"""
スパゲッティ化（Spaghettification）のmanimアニメーション

ブラックホールに近づく物体が潮汐力によって
引き伸ばされる様子を可視化します。
"""

from manim import *


class Spaghettification(Scene):
    """ブラックホールによるスパゲッティ化のアニメーション"""

    def construct(self):
        # タイトル
        title = Text("スパゲッティ化", font_size=48)
        subtitle = Text("Spaghettification", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(0.5)

        # ブラックホールを作成（右側）
        black_hole = Circle(radius=1.2, color=BLACK, fill_opacity=1)
        black_hole.set_stroke(color=PURPLE, width=4)
        # 降着円盤のエフェクト
        accretion_disk = Annulus(
            inner_radius=1.2,
            outer_radius=1.8,
            color=ORANGE,
            fill_opacity=0.3,
        )
        bh_label = Text("ブラックホール", font_size=20)
        bh_group = VGroup(black_hole, accretion_disk)
        bh_group.move_to(RIGHT * 4)
        bh_label.next_to(bh_group, DOWN)

        self.play(
            GrowFromCenter(black_hole),
            FadeIn(accretion_disk),
            Write(bh_label),
        )
        self.wait(0.5)

        # 人型を作成（楕円体として表現）
        person = self.create_person()
        person.move_to(LEFT * 4)

        self.play(FadeIn(person))
        self.wait(0.5)

        # 潮汐力の説明テキスト
        tidal_text = Text(
            "頭と足で重力の強さが違う",
            font_size=24,
        )
        tidal_text.to_edge(DOWN)
        self.play(Write(tidal_text))
        self.wait(1)

        # 潮汐力を示す矢印を追加
        arrows, labels = self.create_tidal_arrows(person)
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            *[FadeIn(label) for label in labels],
        )
        self.wait(1)

        # 説明を更新
        stretch_text = Text(
            "→ 体が引き伸ばされる！",
            font_size=24,
        )
        stretch_text.to_edge(DOWN)
        self.play(Transform(tidal_text, stretch_text))
        self.wait(0.5)

        # スパゲッティ化アニメーション
        # 人がブラックホールに近づきながら引き伸ばされる
        self.play(
            person.animate.move_to(RIGHT * 0.5).stretch(3, 1).stretch(0.3, 0),
            *[FadeOut(arrow) for arrow in arrows],
            *[FadeOut(label) for label in labels],
            run_time=3,
        )
        self.wait(0.5)

        # さらに引き伸ばし
        self.play(
            person.animate.move_to(RIGHT * 2).stretch(2, 1).stretch(0.5, 0),
            run_time=2,
        )
        self.wait(0.5)

        # ブラックホールに吸い込まれる
        self.play(
            person.animate.move_to(RIGHT * 4).scale(0.1),
            run_time=1.5,
        )
        self.wait(0.5)

        # 結論テキスト
        conclusion = Text(
            "これが「スパゲッティ化」です",
            font_size=28,
            color=YELLOW,
        )
        conclusion.to_edge(DOWN)
        self.play(Transform(tidal_text, conclusion))
        self.wait(2)

    def create_person(self) -> VGroup:
        """人型を作成（シンプルな棒人間）"""
        # 頭
        head = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
        head.move_to(UP * 1)

        # 体
        body = Line(UP * 0.75, DOWN * 0.5, color=BLUE, stroke_width=6)

        # 腕
        left_arm = Line(UP * 0.5 + LEFT * 0.4, UP * 0.5, color=BLUE, stroke_width=4)
        right_arm = Line(UP * 0.5, UP * 0.5 + RIGHT * 0.4, color=BLUE, stroke_width=4)

        # 脚
        left_leg = Line(DOWN * 0.5, DOWN * 1 + LEFT * 0.3, color=BLUE, stroke_width=4)
        right_leg = Line(DOWN * 0.5, DOWN * 1 + RIGHT * 0.3, color=BLUE, stroke_width=4)

        person = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        return person

    def create_tidal_arrows(self, person: VGroup) -> tuple[list, list]:
        """潮汐力を示す矢印を作成"""
        # 頭を上に引っ張る力（ブラックホールから遠ざかる方向）
        head_pos = person.get_top()
        head_arrow = Arrow(
            head_pos,
            head_pos + UP * 0.8,
            color=RED,
            stroke_width=4,
        )
        head_label = Text("弱い重力", font_size=16, color=RED)
        head_label.next_to(head_arrow, UP, buff=0.1)

        # 足を下に引っ張る力（ブラックホールに近い＝強い重力）
        foot_pos = person.get_bottom()
        foot_arrow = Arrow(
            foot_pos,
            foot_pos + DOWN * 0.8,
            color=RED,
            stroke_width=4,
        )
        foot_label = Text("強い重力", font_size=16, color=RED)
        foot_label.next_to(foot_arrow, DOWN, buff=0.1)

        arrows = [head_arrow, foot_arrow]
        labels = [head_label, foot_label]
        return arrows, labels


class SpaghettificationBall(Scene):
    """ボールがブラックホールに吸い込まれてスパゲッティ化するアニメーション"""

    def construct(self):
        # ブラックホールを作成（右側）
        black_hole = Circle(radius=1.0, color=BLACK, fill_opacity=1)
        black_hole.set_stroke(color=PURPLE, width=4)
        # 降着円盤のエフェクト
        accretion_disk = Annulus(
            inner_radius=1.0,
            outer_radius=1.6,
            color=ORANGE,
            fill_opacity=0.4,
        )
        # 事象の地平面を示すリング
        event_horizon = Circle(radius=1.0, color=RED, stroke_width=2)

        bh_group = VGroup(accretion_disk, black_hole, event_horizon)
        bh_group.move_to(RIGHT * 4.5)

        self.play(GrowFromCenter(bh_group))
        self.wait(0.3)

        # ボールを作成（左側）
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=0.9)
        ball.set_stroke(color=WHITE, width=2)
        ball.move_to(LEFT * 5)

        self.play(FadeIn(ball))
        self.wait(0.3)

        # 説明テキスト
        text = Text("ボールがブラックホールに近づくと...", font_size=24)
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(0.5)

        # フェーズ1: ボールが近づき始める（少し引き伸ばし開始）
        self.play(
            ball.animate.move_to(LEFT * 2).stretch(1.3, 0).stretch(0.85, 1),
            run_time=1.5,
        )

        # 潮汐力の矢印を表示
        arrow_towards = Arrow(
            ball.get_right(),
            ball.get_right() + RIGHT * 0.8,
            color=RED,
            stroke_width=3,
        )
        arrow_away = Arrow(
            ball.get_left(),
            ball.get_left() + LEFT * 0.5,
            color=ORANGE,
            stroke_width=3,
        )

        text2 = Text("潮汐力で引き伸ばされる", font_size=24)
        text2.to_edge(UP)
        self.play(
            Transform(text, text2),
            GrowArrow(arrow_towards),
            GrowArrow(arrow_away),
        )
        self.wait(0.5)

        # フェーズ2: さらに近づいて引き伸ばされる
        self.play(
            ball.animate.move_to(RIGHT * 0.5).stretch(2.0, 0).stretch(0.5, 1),
            arrow_towards.animate.move_to(RIGHT * 2),
            arrow_away.animate.move_to(LEFT * 0.5),
            run_time=2,
        )
        self.wait(0.3)

        # 矢印をフェードアウト
        self.play(FadeOut(arrow_towards), FadeOut(arrow_away))

        # フェーズ3: スパゲッティ状に引き伸ばされる
        text3 = Text("スパゲッティのように！", font_size=24, color=YELLOW)
        text3.to_edge(UP)
        self.play(
            ball.animate.move_to(RIGHT * 2.5).stretch(3.0, 0).stretch(0.3, 1),
            Transform(text, text3),
            run_time=2,
        )
        self.wait(0.3)

        # フェーズ4: 事象の地平面に到達して吸い込まれる
        # ブラックホール中心は RIGHT * 4.5、半径1.0 なので事象の地平面は RIGHT * 3.5
        self.play(
            ball.animate.move_to(RIGHT * 3.5).stretch(1.5, 0).stretch(0.5, 1),
            run_time=1.5,
            rate_func=rate_functions.ease_in_cubic,
        )

        # 事象の地平面で消える
        self.play(
            ball.animate.scale(0.01),
            run_time=0.5,
            rate_func=rate_functions.ease_in_expo,
        )

        # 結論
        conclusion = Text("これがスパゲッティ化", font_size=28, color=GREEN)
        conclusion.to_edge(UP)
        self.play(Transform(text, conclusion))
        self.wait(2)


class SpaghettificationEarth(Scene):
    """地球上でも起きているスパゲッティ化（とても小さい）"""

    def construct(self):
        # タイトル
        title = Text("地球でも同じことが起きている！", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # 地球
        earth = Circle(radius=2, color=BLUE, fill_opacity=0.6)
        earth.set_stroke(color=GREEN, width=3)
        earth_label = Text("地球", font_size=20)
        earth_label.next_to(earth, DOWN)
        earth.move_to(DOWN * 2)
        earth_label.next_to(earth, DOWN)

        self.play(GrowFromCenter(earth), Write(earth_label))

        # 人（地球の上に立っている）
        person = self.create_small_person()
        person.move_to(UP * 0.5)

        self.play(FadeIn(person))
        self.wait(0.5)

        # 重力の差を示す
        head_text = Text("頭: 地球から少し遠い", font_size=18, color=YELLOW)
        foot_text = Text("足: 地球に近い", font_size=18, color=ORANGE)
        head_text.next_to(person, RIGHT, buff=0.5).shift(UP * 0.3)
        foot_text.next_to(person, RIGHT, buff=0.5).shift(DOWN * 0.3)

        self.play(Write(head_text), Write(foot_text))
        self.wait(1)

        # 矢印（とても小さい効果を示す）
        small_arrow_up = Arrow(
            person.get_top(),
            person.get_top() + UP * 0.3,
            color=RED,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )
        small_arrow_down = Arrow(
            person.get_bottom(),
            person.get_bottom() + DOWN * 0.3,
            color=RED,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )

        effect_text = Text(
            "効果はとても小さい（目に見えない）",
            font_size=20,
            color=GRAY,
        )
        effect_text.to_edge(DOWN)

        self.play(
            GrowArrow(small_arrow_up),
            GrowArrow(small_arrow_down),
            Write(effect_text),
        )
        self.wait(1)

        # 結論
        conclusion = Text(
            "でも原理はブラックホールと同じ！",
            font_size=24,
            color=GREEN,
        )
        conclusion.to_edge(DOWN)
        self.play(Transform(effect_text, conclusion))
        self.wait(2)

    def create_small_person(self) -> VGroup:
        """小さい人型を作成"""
        head = Circle(radius=0.15, color=BLUE, fill_opacity=0.8)
        head.move_to(UP * 0.6)
        body = Line(UP * 0.45, DOWN * 0.3, color=BLUE, stroke_width=4)
        left_leg = Line(DOWN * 0.3, DOWN * 0.6 + LEFT * 0.15, color=BLUE, stroke_width=3)
        right_leg = Line(DOWN * 0.3, DOWN * 0.6 + RIGHT * 0.15, color=BLUE, stroke_width=3)
        return VGroup(head, body, left_leg, right_leg)


if __name__ == "__main__":
    # コマンドラインから実行する場合のヘルプ
    print("使用方法:")
    print("  manim -pql spaghettification.py Spaghettification")
    print("  manim -pql spaghettification.py SpaghettificationBall")
    print("  manim -pql spaghettification.py SpaghettificationEarth")
    print("")
    print("オプション:")
    print("  -p: プレビュー（再生）")
    print("  -ql: 低品質（高速）")
    print("  -qm: 中品質")
    print("  -qh: 高品質")
