"""
縦に並べた2つのボールが離れていくアニメーション
Animation: Two vertically aligned balls diverge while falling

地球に近い下のボールの方が強い重力を受けるので、
より速く落ちて、上のボールとの距離はどんどん開いていきます。

The lower ball, being closer to Earth, experiences stronger gravity,
so it falls faster and the distance from the upper ball keeps increasing.
"""

from manim import *
import numpy as np


class DivergingBalls(Scene):
    """
    縦に並べた2つのボールが離れていく様子を示すアニメーション
    Animation showing two vertically aligned balls diverging while falling
    """

    def construct(self):
        # 地球を作成（透明度を持たせて内部が見えるように）
        # Create Earth (semi-transparent to show interior)
        earth_radius = 2.0
        earth_center = DOWN * 1.5  # 地球を下に移動 / Move Earth down
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.3)
        earth.set_stroke(color=BLUE_B, width=4)
        earth.move_to(earth_center)

        # 地球のラベル
        # Earth label
        earth_label = Text("地球 / Earth", font_size=20, color=BLUE_B)
        earth_label.next_to(earth, DOWN, buff=0.3)

        # 地球の中心点
        # Earth's center point
        center_dot = Dot(earth_center, radius=0.08, color=WHITE)
        center_label = Text("中心 / Center", font_size=16, color=WHITE)
        center_label.next_to(center_dot, DOWN, buff=0.15)

        # シーンを表示
        # Display scene
        self.play(GrowFromCenter(earth), Write(earth_label))
        self.play(FadeIn(center_dot), Write(center_label))
        self.wait(0.5)

        # ボールの設定
        # Ball settings
        ball_radius = 0.12
        vertical_spacing = 0.8  # ボール間の縦の距離 / Vertical distance between balls
        start_height = 2.8  # 地球中心からの高さ（下のボール） / Height from Earth's center (lower ball)

        # 下のボール（赤）- 地球に近い
        # Lower ball (red) - closer to Earth
        ball_lower = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_lower.set_stroke(color=WHITE, width=2)
        ball_lower.move_to(earth_center + UP * start_height)

        # 上のボール（青）- 地球から遠い
        # Upper ball (blue) - farther from Earth
        ball_upper = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_upper.set_stroke(color=WHITE, width=2)
        ball_upper.move_to(earth_center + UP * (start_height + vertical_spacing))

        # ボールを表示
        # Display balls
        self.play(
            GrowFromCenter(ball_lower),
            GrowFromCenter(ball_upper),
        )
        self.wait(0.3)

        # 重力の方向を示す矢印（異なる長さで重力の強さを表現）
        # Gravity arrows with different lengths to show gravity strength
        lower_pos = ball_lower.get_center()
        upper_pos = ball_upper.get_center()

        # 下のボールは強い重力（長い矢印）
        # Lower ball has stronger gravity (longer arrow)
        gravity_lower = Arrow(
            lower_pos + DOWN * 0.2,
            lower_pos + DOWN * 1.2,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        gravity_lower_label = Text("強い重力", font_size=14, color=YELLOW)
        gravity_lower_label_en = Text("Strong gravity", font_size=10, color=YELLOW_A)
        gravity_lower_group = VGroup(gravity_lower_label, gravity_lower_label_en).arrange(DOWN, buff=0.05)
        gravity_lower_group.next_to(gravity_lower, RIGHT, buff=0.1)

        # 上のボールは弱い重力（短い矢印）
        # Upper ball has weaker gravity (shorter arrow)
        gravity_upper = Arrow(
            upper_pos + DOWN * 0.2,
            upper_pos + DOWN * 0.7,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )
        gravity_upper_label = Text("弱い重力", font_size=14, color=ORANGE)
        gravity_upper_label_en = Text("Weak gravity", font_size=10, color=ORANGE)
        gravity_upper_group = VGroup(gravity_upper_label, gravity_upper_label_en).arrange(DOWN, buff=0.05)
        gravity_upper_group.next_to(gravity_upper, RIGHT, buff=0.1)

        # 説明テキスト
        # Explanation text
        text1 = Text(
            "地球に近い方が重力が強い",
            font_size=24,
        )
        text1_en = Text(
            "Closer to Earth = Stronger gravity",
            font_size=18,
            color=GRAY,
        )
        text_group = VGroup(text1, text1_en).arrange(DOWN, buff=0.1)
        text_group.to_edge(UP)

        self.play(
            Write(text_group),
            GrowArrow(gravity_lower),
            GrowArrow(gravity_upper),
            FadeIn(gravity_lower_group),
            FadeIn(gravity_upper_group),
        )
        self.wait(1.5)

        # 矢印とラベルをフェードアウト
        # Fade out arrows and labels
        self.play(
            FadeOut(gravity_lower),
            FadeOut(gravity_upper),
            FadeOut(gravity_lower_group),
            FadeOut(gravity_upper_group),
        )

        # 説明テキストを更新
        # Update explanation text
        text2 = Text(
            "下のボールの方が速く落ちる",
            font_size=24,
        )
        text2_en = Text(
            "The lower ball falls faster",
            font_size=18,
            color=GRAY,
        )
        text_group2 = VGroup(text2, text2_en).arrange(DOWN, buff=0.1)
        text_group2.to_edge(UP)

        self.play(Transform(text_group, text_group2))
        self.wait(0.5)

        # ボール間の距離を示す両矢印（初期）
        # Double arrow showing distance between balls (initial)
        distance_arrow = DoubleArrow(
            ball_lower.get_center() + RIGHT * 0.3,
            ball_upper.get_center() + RIGHT * 0.3,
            color=GREEN,
            stroke_width=2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(GrowFromCenter(distance_arrow))
        self.wait(0.3)

        # 落下アニメーション（下のボールがより速く落ちる）
        # Fall animation (lower ball falls faster)
        fall_duration = 2.5

        # 最終位置を計算（下のボールはより多く落下）
        # Calculate final positions (lower ball falls more)
        lower_final = earth_center + UP * 0.5  # 地球中心近くまで落下
        upper_final = earth_center + UP * 1.8  # 上のボールはそこまで落ちない

        # 距離矢印も更新しながら落下
        # Fall while updating distance arrow
        self.play(
            ball_lower.animate.move_to(lower_final),
            ball_upper.animate.move_to(upper_final),
            distance_arrow.animate.put_start_and_end_on(
                lower_final + RIGHT * 0.3,
                upper_final + RIGHT * 0.3,
            ),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 結論テキスト
        # Conclusion text
        conclusion = Text(
            "2つのボールは離れていく！",
            font_size=28,
            color=GREEN,
        )
        conclusion_en = Text(
            "The two balls move apart!",
            font_size=20,
            color=GREEN_A,
        )
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(UP)

        self.play(Transform(text_group, conclusion_group))
        self.wait(2)


class DivergingBallsSimple(Scene):
    """
    シンプル版：縦に並べた2つのボールが離れていく
    Simple version: Two vertically aligned balls diverge
    """

    def construct(self):
        # 地球を作成
        # Create Earth
        earth_radius = 1.8
        earth_center = DOWN * 1.5  # 地球を下に移動 / Move Earth down
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.25)
        earth.set_stroke(color=BLUE_B, width=3)
        earth.move_to(earth_center)

        # 地球の中心点
        # Earth's center
        center_dot = Dot(earth_center, radius=0.06, color=WHITE)

        self.add(earth, center_dot)
        self.wait(0.3)

        # ボールの設定
        # Ball settings
        ball_radius = 0.1
        vertical_spacing = 0.6
        start_height = 2.8

        # ボールを作成
        # Create balls
        ball_lower = Circle(radius=ball_radius, color="#e74c3c", fill_opacity=0.9)
        ball_lower.set_stroke(color=WHITE, width=2)
        ball_lower.move_to(earth_center + UP * start_height)

        ball_upper = Circle(radius=ball_radius, color="#3498db", fill_opacity=0.9)
        ball_upper.set_stroke(color=WHITE, width=2)
        ball_upper.move_to(earth_center + UP * (start_height + vertical_spacing))

        # ボールを表示
        # Display balls
        self.play(
            FadeIn(ball_lower, scale=0.5),
            FadeIn(ball_upper, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.5)

        # 落下アニメーション
        # Fall animation
        lower_final = earth_center + UP * 0.5
        upper_final = earth_center + UP * 1.6

        self.play(
            ball_lower.animate.move_to(lower_final),
            ball_upper.animate.move_to(upper_final),
            run_time=2.0,
            rate_func=rate_functions.ease_in_quad,
        )

        self.wait(1.5)


class DivergingBallsWithLabels(Scene):
    """
    ラベル付き版：縦に並べた2つのボールが離れていく
    Labeled version: Two vertically aligned balls diverge
    """

    def construct(self):
        # タイトル
        # Title
        title = Text("縦に並べたボールを落とすと？", font_size=26)
        title_en = Text(
            "What happens when we drop vertically aligned balls?",
            font_size=16,
            color=GRAY,
        )
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP)

        self.play(Write(title_group))
        self.wait(0.3)

        # 地球を作成
        # Create Earth
        earth_radius = 1.8
        center_pos = DOWN * 1.5
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.25)
        earth.set_stroke(color=BLUE_B, width=3)
        earth.move_to(center_pos)

        # 地球の中心点とラベル
        # Earth's center and label
        center_dot = Dot(center_pos, radius=0.08, color=WHITE)
        center_label = Text("中心", font_size=14, color=WHITE)
        center_label.next_to(center_dot, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(earth),
            FadeIn(center_dot),
            Write(center_label),
        )
        self.wait(0.3)

        # ボールの設定
        # Ball settings
        ball_radius = 0.11
        vertical_spacing = 0.7
        start_height = 2.8

        # ボールを作成
        # Create balls
        ball_lower = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_lower.set_stroke(color=WHITE, width=2)
        lower_start = center_pos + UP * start_height

        ball_upper = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_upper.set_stroke(color=WHITE, width=2)
        upper_start = center_pos + UP * (start_height + vertical_spacing)

        ball_lower.move_to(lower_start)
        ball_upper.move_to(upper_start)

        # ボール間の距離を示す矢印（初期）
        # Arrow showing initial distance between balls
        initial_distance_arrow = DoubleArrow(
            lower_start + LEFT * 0.4,
            upper_start + LEFT * 0.4,
            color=YELLOW,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.15,
        )
        initial_distance_label = Text("初期間隔", font_size=12, color=YELLOW)
        initial_distance_label.next_to(initial_distance_arrow, LEFT, buff=0.1)

        self.play(
            GrowFromCenter(ball_lower),
            GrowFromCenter(ball_upper),
        )
        self.play(
            GrowFromCenter(initial_distance_arrow),
            FadeIn(initial_distance_label),
        )
        self.wait(0.5)

        # 重力の強さを示す矢印
        # Gravity strength arrows
        gravity_lower = Arrow(
            lower_start + DOWN * 0.2,
            lower_start + DOWN * 1.0,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )
        gravity_upper = Arrow(
            upper_start + DOWN * 0.2,
            upper_start + DOWN * 0.6,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )

        self.play(
            GrowArrow(gravity_lower),
            GrowArrow(gravity_upper),
        )
        self.wait(0.5)

        # 矢印と初期距離表示をフェードアウト
        # Fade out arrows and initial distance display
        self.play(
            FadeOut(gravity_lower),
            FadeOut(gravity_upper),
            FadeOut(initial_distance_arrow),
            FadeOut(initial_distance_label),
        )

        # 落下アニメーション
        # Fall animation
        fall_duration = 2.5
        lower_final = center_pos + UP * 0.5
        upper_final = center_pos + UP * 1.7

        # 距離が広がる様子を示すテキスト
        # Text showing increasing distance
        expanding_text = Text("間隔が広がる...", font_size=20, color=GREEN)
        expanding_text_en = Text("Distance increasing...", font_size=14, color=GREEN_A)
        expanding_group = VGroup(expanding_text, expanding_text_en).arrange(DOWN, buff=0.05)
        expanding_group.to_edge(RIGHT).shift(UP * 0.5)

        self.play(
            ball_lower.animate.move_to(lower_final),
            ball_upper.animate.move_to(upper_final),
            FadeIn(expanding_group),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 最終距離を示す矢印
        # Arrow showing final distance
        final_distance_arrow = DoubleArrow(
            lower_final + LEFT * 0.4,
            upper_final + LEFT * 0.4,
            color=GREEN,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.1,
        )
        final_distance_label = Text("広がった！", font_size=14, color=GREEN)
        final_distance_label.next_to(final_distance_arrow, LEFT, buff=0.1)

        self.play(
            GrowFromCenter(final_distance_arrow),
            FadeIn(final_distance_label),
            FadeOut(expanding_group),
        )

        # 結論
        # Conclusion
        conclusion = Text("離れていく！", font_size=24, color=GREEN)
        conclusion_en = Text("They move apart!", font_size=16, color=GREEN_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN)

        self.play(Write(conclusion_group))
        self.wait(2)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/diverging_balls.py DivergingBalls")
    print("  manim -pql scripts/diverging_balls.py DivergingBallsSimple")
    print("  manim -pql scripts/diverging_balls.py DivergingBallsWithLabels")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  DivergingBalls       - 基本版（説明テキスト・重力矢印付き）")
    print("                         Basic version with explanation text and gravity arrows")
    print("  DivergingBallsSimple - シンプル版（最小構成）")
    print("                         Simple version (minimal)")
    print("  DivergingBallsWithLabels - ラベル付き版（距離表示あり）")
    print("                             Labeled version with distance indicators")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
