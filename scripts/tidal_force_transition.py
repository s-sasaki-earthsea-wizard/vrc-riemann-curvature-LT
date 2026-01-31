"""
等価原理から潮汐力への転換アニメーション
Transition animation from Equivalence Principle to Tidal Forces

自由落下で重力が「消えた」ように見えても、
潮汐力という「消せない本物の重力効果」があることを示す。
エレベーターが潮汐力で変形することで視覚化。

Shows that even though gravity seems to "disappear" in free fall,
there exists an "uncancellable real gravity effect" - tidal forces.
Visualized by the elevator deforming due to tidal forces.

脚本L58-64に対応：
「でも重力を完全に『消せる』なら、重力って本当に存在するのかわからないような気がしてきませんか？」
「実は、そうではありません。」
「自由落下しても消せない、『本物の』重力効果があるんです。」
「それが、さっき話した潮汐力なんですね。」
"""

from manim import *


def create_text_with_backplate(
    text_content, font_size, text_color, bg_color="#000000", bg_opacity=0.7, padding=0.15
):
    """
    バックプレート付きテキストを作成するヘルパー関数
    Helper function to create text with a background plate
    """
    text = Text(text_content, font_size=font_size, color=text_color)
    backplate = Rectangle(
        width=text.width + padding * 2,
        height=text.height + padding * 2,
        color=bg_color,
        fill_color=bg_color,
        fill_opacity=bg_opacity,
        stroke_width=0,
    )
    backplate.move_to(text.get_center())
    return VGroup(backplate, text)


class TidalForceTransition(Scene):
    """
    等価原理から潮汐力への転換シーン（約20秒）
    Transition scene from Equivalence Principle to Tidal Forces (~20 seconds)
    """

    def construct(self):
        # 背景色を設定
        # Set background color
        self.camera.background_color = "#1a1a2e"

        # === フェーズ1: 自由落下エレベーター（無重力状態） ===
        # === Phase 1: Free-falling elevator (weightless state) ===

        # エレベーター（箱）を作成
        # Create elevator (box)
        elevator_width = 3.5
        elevator_height = 4.5
        elevator = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY,
            fill_opacity=0.15,
        )
        elevator.set_stroke(color=WHITE, width=4)
        elevator.move_to(LEFT * 2.5)

        # 人（棒人間）を作成
        # Create person (stick figure)
        person = self.create_stick_figure()
        person.move_to(elevator.get_center())

        # 自由落下中のラベル
        # Free fall label
        freefall_label = create_text_with_backplate(
            "自由落下中 / In Free Fall",
            font_size=22,
            text_color=BLUE_B,
            bg_opacity=0.8,
        )
        freefall_label.next_to(elevator, UP, buff=0.3)

        # 下向きの運動を示す矢印（エレベーター全体）
        # Arrow showing downward motion (entire elevator)
        motion_arrow = Arrow(
            start=elevator.get_bottom() + DOWN * 0.3,
            end=elevator.get_bottom() + DOWN * 1.5,
            color=GRAY,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )
        motion_label = Text("↓ 落下中", font_size=16, color=GRAY)
        motion_label.next_to(motion_arrow, RIGHT, buff=0.1)

        # 表示
        # Display
        self.play(
            FadeIn(elevator),
            FadeIn(person),
            FadeIn(freefall_label),
            run_time=0.8,
        )
        self.play(
            GrowArrow(motion_arrow),
            FadeIn(motion_label),
            run_time=0.5,
        )
        self.wait(0.5)

        # 無重力状態のテキスト
        # Weightless state text
        weightless_text = create_text_with_backplate(
            "重力が「消えた」？\nDid gravity 'disappear'?",
            font_size=26,
            text_color=GREEN,
            bg_opacity=0.85,
        )
        weightless_text.move_to(RIGHT * 3.0 + UP * 2.0)

        self.play(FadeIn(weightless_text), run_time=0.6)
        self.wait(1.0)

        # === フェーズ2: 疑問から転換 ===
        # === Phase 2: Transition from question ===

        # 疑問マークを表示
        # Show question mark
        question = Text("？", font_size=100, color=YELLOW)
        question.move_to(RIGHT * 3.0 + DOWN * 0.5)

        self.play(FadeIn(question, scale=1.3), run_time=0.5)
        self.wait(0.8)

        # 「実は...」のテキスト
        # "Actually..." text
        actually_text = create_text_with_backplate(
            "実は... / Actually...",
            font_size=28,
            text_color=ORANGE,
            bg_opacity=0.85,
        )
        actually_text.move_to(RIGHT * 3.0 + DOWN * 2.0)

        self.play(
            FadeOut(question),
            FadeIn(actually_text),
            run_time=0.6,
        )
        self.wait(0.8)

        # === フェーズ3: 潮汐力の矢印を表示 ===
        # === Phase 3: Show tidal force arrows ===

        # 右側のテキストを更新
        # Update right side text
        self.play(
            FadeOut(weightless_text),
            FadeOut(actually_text),
            run_time=0.4,
        )

        # 潮汐力の説明テキスト
        # Tidal force explanation text
        tidal_explain = create_text_with_backplate(
            "消せない重力効果\nUncancellable gravity effect",
            font_size=24,
            text_color=WHITE,
            bg_opacity=0.85,
        )
        tidal_explain.move_to(RIGHT * 3.0 + UP * 2.5)

        self.play(FadeIn(tidal_explain), run_time=0.5)

        # 潮汐力の矢印（tidal_stretch_body.pyと同じスタイル）
        # Tidal force arrows (same style as tidal_stretch_body.py)
        # 相対論の文脈では、重力はすべて地球の中心（下）を向く
        # In GR context, gravity points toward Earth's center (down)
        # 長さの違いで重力の強さの差を表現
        # Length difference shows gravity strength difference

        elevator_top = elevator.get_top()
        elevator_bottom = elevator.get_bottom()
        elevator_left = elevator.get_left()
        elevator_right = elevator.get_right()

        # 上部への重力（短い矢印 = 重力が弱い）
        # Gravity at top (shorter arrow = weaker gravity)
        gravity_top = Arrow(
            start=elevator_top + LEFT * 0.6,
            end=elevator_top + LEFT * 0.6 + DOWN * 0.7,
            color=RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )

        # 下部への重力（長い矢印 = 重力が強い）
        # Gravity at bottom (longer arrow = stronger gravity)
        gravity_bottom = Arrow(
            start=elevator_bottom + LEFT * 0.6 + UP * 0.3,
            end=elevator_bottom + LEFT * 0.6 + UP * 0.3 + DOWN * 1.2,
            color=RED,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )

        # 横方向の圧縮矢印（地球中心方向に引かれる）
        # Horizontal compression arrows (pulled toward Earth's center)
        compress_left = Arrow(
            start=elevator_left + LEFT * 0.5 + UP * 0.2,
            end=elevator_left + RIGHT * 0.2 + DOWN * 0.3,
            color=BLUE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )
        compress_right = Arrow(
            start=elevator_right + RIGHT * 0.5 + UP * 0.2,
            end=elevator_right + LEFT * 0.2 + DOWN * 0.3,
            color=BLUE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )

        # 矢印のラベル（tidal_stretch_body.pyと同じスタイル）
        # Arrow labels (same style as tidal_stretch_body.py)
        gravity_label_top = create_text_with_backplate(
            "g（弱）/ g (weak)",
            font_size=18,
            text_color=RED,
            bg_opacity=0.85,
        )
        gravity_label_top.next_to(gravity_top, LEFT, buff=0.15)

        gravity_label_bottom = create_text_with_backplate(
            "g（強）/ g (strong)",
            font_size=18,
            text_color=RED,
            bg_opacity=0.85,
        )
        gravity_label_bottom.next_to(gravity_bottom, LEFT, buff=0.15)

        stretch_effect_label = create_text_with_backplate(
            "→ 縦に引き伸ばされる\n→ Stretched vertically",
            font_size=20,
            text_color=RED,
            bg_opacity=0.85,
        )
        stretch_effect_label.move_to(RIGHT * 3.0 + UP * 0.8)

        compress_label = create_text_with_backplate(
            "横に圧縮\nHorizontal squeeze",
            font_size=20,
            text_color=BLUE,
            bg_opacity=0.85,
        )
        compress_label.move_to(RIGHT * 3.0 + DOWN * 0.5)

        # 縦方向の矢印を表示
        # Show vertical arrows
        self.play(
            GrowArrow(gravity_top),
            GrowArrow(gravity_bottom),
            FadeIn(gravity_label_top),
            FadeIn(gravity_label_bottom),
            run_time=0.7,
        )
        self.wait(0.3)

        # 引き伸ばし効果のラベル
        # Stretch effect label
        self.play(
            FadeIn(stretch_effect_label),
            run_time=0.5,
        )
        self.wait(0.3)

        # 横方向の矢印を表示
        # Show horizontal arrows
        self.play(
            GrowArrow(compress_left),
            GrowArrow(compress_right),
            FadeIn(compress_label),
            run_time=0.7,
        )
        self.wait(0.5)

        # === フェーズ4: エレベーターの変形 ===
        # === Phase 4: Elevator deformation ===

        # エレベーターと人を変形（誇張表現）
        # Deform elevator and person (exaggerated)
        deform_group = VGroup(elevator, person)

        self.play(
            deform_group.animate.stretch(1.08, dim=1).stretch(0.93, dim=0),
            gravity_top.animate.shift(DOWN * 0.1),
            gravity_label_top.animate.shift(DOWN * 0.1),
            gravity_bottom.animate.shift(DOWN * 0.15),
            gravity_label_bottom.animate.shift(DOWN * 0.15),
            compress_left.animate.shift(RIGHT * 0.1),
            compress_right.animate.shift(LEFT * 0.1),
            run_time=1.2,
            rate_func=rate_functions.ease_out_quad,
        )
        self.wait(0.5)

        # === フェーズ5: テロップ表示 ===
        # === Phase 5: Show telop ===

        # 右側のラベルをフェードアウト
        # Fade out right side labels
        self.play(
            FadeOut(tidal_explain),
            FadeOut(gravity_label_top),
            FadeOut(gravity_label_bottom),
            FadeOut(stretch_effect_label),
            FadeOut(compress_label),
            run_time=0.4,
        )

        # メインテロップ（画面中央右）
        # Main telop (center-right of screen)
        telop_main = Text(
            "潮汐力",
            font_size=48,
            color=YELLOW,
            weight=BOLD,
        )
        telop_sub = Text(
            "消せない本物の重力",
            font_size=32,
            color=YELLOW,
        )
        telop_en = Text(
            "Tidal Force: The Real Gravity You Can't Cancel",
            font_size=20,
            color=YELLOW_C,
        )

        telop_group = VGroup(telop_main, telop_sub, telop_en).arrange(DOWN, buff=0.2)
        telop_group.move_to(RIGHT * 2.8)

        # テロップ用バックプレート
        # Backplate for telop
        telop_backplate = Rectangle(
            width=telop_group.width + 0.5,
            height=telop_group.height + 0.4,
            color="#000000",
            fill_color="#000000",
            fill_opacity=0.85,
            stroke_width=2,
            stroke_color=YELLOW,
        )
        telop_backplate.move_to(telop_group.get_center())

        telop_with_bg = VGroup(telop_backplate, telop_group)

        self.play(
            FadeIn(telop_with_bg, scale=0.95),
            run_time=0.8,
        )

        # テロップを強調
        # Emphasize telop
        self.play(
            telop_with_bg.animate.scale(1.05),
            run_time=0.25,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            telop_with_bg.animate.scale(1 / 1.05),
            run_time=0.25,
            rate_func=rate_functions.ease_in_quad,
        )

        # 静止
        # Hold
        self.wait(2.5)

        # === フェーズ6: 次セクションへのブリッジ ===
        # === Phase 6: Bridge to next section ===

        # すべてをフェードアウト
        # Fade out everything
        all_objects = VGroup(
            elevator,
            person,
            freefall_label,
            motion_arrow,
            motion_label,
            gravity_top,
            gravity_bottom,
            compress_left,
            compress_right,
            telop_with_bg,
        )

        self.play(
            FadeOut(all_objects),
            run_time=0.8,
        )

        # 次のセクションへの導入テキスト
        # Introduction text to next section
        next_section = create_text_with_backplate(
            "では、潮汐力を詳しく見ていきましょう\nLet's examine tidal forces in detail",
            font_size=28,
            text_color=WHITE,
            bg_opacity=0.9,
        )
        next_section.move_to(ORIGIN)

        self.play(FadeIn(next_section, scale=0.9), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(next_section), run_time=0.5)
        self.wait(0.3)

    def create_stick_figure(self):
        """
        シンプルな棒人間を作成（浮いている姿勢）
        Create a simple stick figure (floating posture)
        """
        # 頭 / Head
        head = Circle(radius=0.25, color=WHITE, fill_opacity=0.6)
        head.set_stroke(color=WHITE, width=3)

        # 体 / Body
        body = Line(ORIGIN, DOWN * 0.8, color=WHITE, stroke_width=4)
        body.next_to(head, DOWN, buff=0)

        # 腕（少し広げた姿勢）/ Arms (slightly spread)
        left_arm = Line(ORIGIN, LEFT * 0.5 + UP * 0.1, color=WHITE, stroke_width=3)
        right_arm = Line(ORIGIN, RIGHT * 0.5 + UP * 0.1, color=WHITE, stroke_width=3)
        arm_start = body.get_start() + DOWN * 0.15
        left_arm.move_to(arm_start, aligned_edge=RIGHT)
        right_arm.move_to(arm_start, aligned_edge=LEFT)

        # 足（少し広げた姿勢）/ Legs (slightly spread)
        left_leg = Line(ORIGIN, LEFT * 0.25 + DOWN * 0.5, color=WHITE, stroke_width=3)
        right_leg = Line(ORIGIN, RIGHT * 0.25 + DOWN * 0.5, color=WHITE, stroke_width=3)
        leg_start = body.get_end()
        left_leg.move_to(leg_start, aligned_edge=UP + RIGHT * 0.5)
        right_leg.move_to(leg_start, aligned_edge=UP + LEFT * 0.5)

        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)


class TidalForceTransitionShort(Scene):
    """
    短縮版：等価原理から潮汐力への転換（約12秒）
    Short version: Transition from Equivalence Principle to Tidal Forces (~12 seconds)
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # エレベーターと人を作成
        # Create elevator and person
        elevator = Rectangle(
            width=3.0,
            height=4.0,
            color=GRAY,
            fill_opacity=0.15,
        )
        elevator.set_stroke(color=WHITE, width=4)
        elevator.move_to(LEFT * 2.5)

        person = self.create_simple_person()
        person.move_to(elevator.get_center())

        # 表示
        self.play(FadeIn(elevator), FadeIn(person), run_time=0.5)

        # 疑問テキスト
        question_text = create_text_with_backplate(
            "重力が消えた？\nGravity disappeared?",
            font_size=26,
            text_color=GREEN,
            bg_opacity=0.85,
        )
        question_text.move_to(RIGHT * 3.0 + UP * 1.5)

        self.play(FadeIn(question_text), run_time=0.5)
        self.wait(0.8)

        # 潮汐力矢印（両方とも下向き、長さで強さを表現）
        # Tidal force arrows (both pointing down, length shows strength)
        gravity_top = Arrow(
            elevator.get_top() + LEFT * 0.5,
            elevator.get_top() + LEFT * 0.5 + DOWN * 0.6,
            color=RED,
            stroke_width=5,
            buff=0,
        )
        gravity_bottom = Arrow(
            elevator.get_bottom() + LEFT * 0.5 + UP * 0.3,
            elevator.get_bottom() + LEFT * 0.5 + UP * 0.3 + DOWN * 1.0,
            color=RED,
            stroke_width=6,
            buff=0,
        )
        compress_left = Arrow(
            elevator.get_left() + LEFT * 0.4,
            elevator.get_left() + RIGHT * 0.1 + DOWN * 0.2,
            color=BLUE,
            stroke_width=5,
            buff=0,
        )
        compress_right = Arrow(
            elevator.get_right() + RIGHT * 0.4,
            elevator.get_right() + LEFT * 0.1 + DOWN * 0.2,
            color=BLUE,
            stroke_width=5,
            buff=0,
        )

        self.play(
            FadeOut(question_text),
            GrowArrow(gravity_top),
            GrowArrow(gravity_bottom),
            GrowArrow(compress_left),
            GrowArrow(compress_right),
            run_time=0.7,
        )

        # 変形
        deform_group = VGroup(elevator, person)
        self.play(
            deform_group.animate.stretch(1.08, dim=1).stretch(0.93, dim=0),
            gravity_top.animate.shift(DOWN * 0.08),
            gravity_bottom.animate.shift(DOWN * 0.12),
            compress_left.animate.shift(RIGHT * 0.08),
            compress_right.animate.shift(LEFT * 0.08),
            run_time=1.0,
        )

        # テロップ
        telop = create_text_with_backplate(
            "潮汐力: 消せない本物の重力\nTidal Force: The Real Gravity You Can't Cancel",
            font_size=26,
            text_color=YELLOW,
            bg_opacity=0.9,
        )
        telop.move_to(RIGHT * 2.8)

        self.play(FadeIn(telop, scale=0.95), run_time=0.6)
        self.play(telop.animate.scale(1.05), run_time=0.2)
        self.play(telop.animate.scale(1 / 1.05), run_time=0.2)

        self.wait(2.0)

    def create_simple_person(self):
        """シンプルな人の図形 / Simple person shape"""
        head = Circle(radius=0.2, color=WHITE, fill_opacity=0.5)
        head.set_stroke(color=WHITE, width=2)
        body = Line(ORIGIN, DOWN * 0.6, color=WHITE, stroke_width=3)
        body.next_to(head, DOWN, buff=0)
        left_arm = Line(ORIGIN, LEFT * 0.3, color=WHITE, stroke_width=2)
        right_arm = Line(ORIGIN, RIGHT * 0.3, color=WHITE, stroke_width=2)
        arm_pos = body.get_start() + DOWN * 0.1
        left_arm.move_to(arm_pos)
        right_arm.move_to(arm_pos)
        left_leg = Line(ORIGIN, LEFT * 0.15 + DOWN * 0.4, color=WHITE, stroke_width=2)
        right_leg = Line(ORIGIN, RIGHT * 0.15 + DOWN * 0.4, color=WHITE, stroke_width=2)
        leg_pos = body.get_end()
        left_leg.move_to(leg_pos, aligned_edge=UP)
        right_leg.move_to(leg_pos, aligned_edge=UP)
        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)


if __name__ == "__main__":
    # コマンドラインから実行する場合のヘルプ
    # Help for command line execution
    print("使用方法 / Usage:")
    print("  manim -pql scripts/tidal_force_transition.py TidalForceTransition")
    print("  manim -pql scripts/tidal_force_transition.py TidalForceTransitionShort")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  TidalForceTransition      - フル版（約20秒）")
    print("                              Full version (~20 seconds)")
    print("  TidalForceTransitionShort - 短縮版（約12秒）")
    print("                              Short version (~12 seconds)")
    print("")
    print("脚本L58-64に対応 / Corresponds to script L58-64:")
    print("  「でも重力を完全に『消せる』なら...」")
    print("  「自由落下しても消せない、『本物の』重力効果があるんです。」")
    print("  「それが、さっき話した潮汐力なんですね。」")
