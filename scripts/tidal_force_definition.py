"""
潮汐力の定義アニメーション（L81-85用）
Animation: Definition of Tidal Force (for L81-85)

重力は加速度と区別できないはずなのに（等価原理）、
自由落下しても消すことができない重力効果 = 潮汐力

Despite gravity being indistinguishable from acceleration (equivalence principle),
tidal force is the gravity effect that cannot be eliminated even in free fall.
"""

from manim import *


class TidalForceDefinition(Scene):
    """
    潮汐力の定義：消せない重力効果
    Definition of Tidal Force: The Inescapable Gravity Effect
    """

    def construct(self):
        # パート1：等価原理の復習
        # Part 1: Recap of equivalence principle
        equiv_title = Text("等価原理", font_size=32, color=BLUE)
        equiv_title_en = Text("Equivalence Principle", font_size=24, color=BLUE_A)
        equiv_group = VGroup(equiv_title, equiv_title_en).arrange(DOWN, buff=0.1)
        equiv_group.to_edge(UP)

        self.play(Write(equiv_group))
        self.wait(0.5)

        # 等価原理の内容
        # Content of equivalence principle
        equiv_text = Text("重力 ≈ 加速度", font_size=36)
        equiv_text_en = Text("Gravity ≈ Acceleration", font_size=24, color=GRAY)
        equiv_content = VGroup(equiv_text, equiv_text_en).arrange(DOWN, buff=0.1)

        self.play(Write(equiv_content))
        self.wait(0.5)

        # 「自由落下で消せる」
        # "Can be eliminated by free fall"
        can_eliminate = Text("→ 自由落下で「消せる」", font_size=28, color=GREEN)
        can_eliminate_en = Text(
            "→ Can be 'eliminated' by free fall", font_size=20, color=GREEN_A
        )
        can_eliminate_group = VGroup(can_eliminate, can_eliminate_en).arrange(
            DOWN, buff=0.1
        )
        can_eliminate_group.next_to(equiv_content, DOWN, buff=0.5)

        self.play(Write(can_eliminate_group))
        self.wait(1)

        # パート2：「でも...」+ エレベーターの簡略版
        # Part 2: "But..." + simplified elevator animation
        but_text = Text("でも...", font_size=40, color=YELLOW)
        but_text_en = Text("But...", font_size=28, color=YELLOW_A)
        but_group = VGroup(but_text, but_text_en).arrange(DOWN, buff=0.1)

        self.play(
            FadeOut(equiv_group),
            FadeOut(equiv_content),
            FadeOut(can_eliminate_group),
        )
        self.play(Write(but_group))
        self.wait(0.5)

        # 「でも」を上に移動
        # Move "But" to top
        but_group.generate_target()
        but_group.target.to_edge(UP)
        self.play(MoveToTarget(but_group))

        # 簡略版エレベーター（2つ横並び）
        # Simplified elevators (two side by side)
        elevator_width = 2.0
        elevator_height = 2.5
        elevator_spacing = 1.0

        # 左のエレベーター（横並びボール）
        left_center = LEFT * (elevator_width / 2 + elevator_spacing / 2) + DOWN * 0.3
        elevator_left = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=2,
        )
        elevator_left.set_fill(color=GRAY_E, opacity=0.2)
        elevator_left.move_to(left_center)

        # 右のエレベーター（縦並びボール）
        right_center = RIGHT * (elevator_width / 2 + elevator_spacing / 2) + DOWN * 0.3
        elevator_right = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=2,
        )
        elevator_right.set_fill(color=GRAY_E, opacity=0.2)
        elevator_right.move_to(right_center)

        # ボール設定
        ball_radius = 0.15

        # 左：横に並べたボール
        h_spacing = 0.9
        ball_h_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_left.set_stroke(color=WHITE, width=2)
        ball_h_left.move_to(left_center + LEFT * (h_spacing / 2))

        ball_h_right = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_right.set_stroke(color=WHITE, width=2)
        ball_h_right.move_to(left_center + RIGHT * (h_spacing / 2))

        # 右：縦に並べたボール
        v_spacing = 0.7
        ball_v_upper = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_v_upper.set_stroke(color=WHITE, width=2)
        ball_v_upper.move_to(right_center + UP * (v_spacing / 2))

        ball_v_lower = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_v_lower.set_stroke(color=WHITE, width=2)
        ball_v_lower.move_to(right_center + DOWN * (v_spacing / 2))

        # エレベーターとボールを表示
        self.play(
            Create(elevator_left),
            Create(elevator_right),
            GrowFromCenter(ball_h_left),
            GrowFromCenter(ball_h_right),
            GrowFromCenter(ball_v_upper),
            GrowFromCenter(ball_v_lower),
            run_time=0.8,
        )
        self.wait(0.3)

        # ボールが動くアニメーション
        h_final_spacing = 0.35
        v_lower_final_y = 0.9

        self.play(
            ball_h_left.animate.move_to(left_center + LEFT * (h_final_spacing / 2)),
            ball_h_right.animate.move_to(left_center + RIGHT * (h_final_spacing / 2)),
            ball_v_lower.animate.move_to(right_center + DOWN * v_lower_final_y),
            run_time=2.0,
            rate_func=rate_functions.linear,
        )

        # ラベル表示
        converge_label = Text("近づく", font_size=14, color=RED_C)
        converge_label.next_to(elevator_left, DOWN, buff=0.15)

        diverge_label = Text("離れる", font_size=14, color=BLUE_C)
        diverge_label.next_to(elevator_right, DOWN, buff=0.15)

        self.play(
            FadeIn(converge_label),
            FadeIn(diverge_label),
        )
        self.wait(0.5)

        # テキスト
        problem_text = Text(
            "自由落下中でも、ボールは動いている", font_size=24, color=ORANGE
        )
        problem_text_en = Text(
            "Even in free fall, the balls are moving", font_size=16, color=ORANGE
        )
        problem_group = VGroup(problem_text, problem_text_en).arrange(DOWN, buff=0.1)
        problem_group.to_edge(DOWN, buff=0.5)

        self.play(Write(problem_group))
        self.wait(1)

        # エレベーターをフェードアウト
        elevator_group = VGroup(
            elevator_left,
            elevator_right,
            ball_h_left,
            ball_h_right,
            ball_v_upper,
            ball_v_lower,
            converge_label,
            diverge_label,
        )

        # パート3：潮汐力の定義
        # Part 3: Definition of tidal force
        self.play(
            FadeOut(but_group),
            FadeOut(problem_group),
            FadeOut(elevator_group),
        )

        # 大きなタイトル
        # Big title
        tidal_title = Text("潮汐力", font_size=48, color=YELLOW)
        tidal_title_en = Text("Tidal Force", font_size=36, color=YELLOW_A)
        tidal_group = VGroup(tidal_title, tidal_title_en).arrange(DOWN, buff=0.15)

        self.play(Write(tidal_group))
        self.wait(0.5)

        # タイトルを上に移動
        # Move title up
        tidal_group.generate_target()
        tidal_group.target.to_edge(UP)
        self.play(MoveToTarget(tidal_group))

        # 定義1：重力の勾配
        # Definition 1: Gravity gradient
        def1 = Text("重力が場所によって違う", font_size=28)
        def1_en = Text("Gravity varies by location", font_size=20, color=GRAY)
        def1_group = VGroup(def1, def1_en).arrange(DOWN, buff=0.1)

        self.play(Write(def1_group))
        self.wait(0.8)

        # 矢印
        arrow = Text("↓", font_size=36, color=YELLOW)
        arrow.next_to(def1_group, DOWN, buff=0.3)
        self.play(Write(arrow))

        # 定義2：消せない効果
        # Definition 2: Cannot be eliminated
        def2 = Text("自由落下しても消すことができない", font_size=28, color=RED)
        def2_en = Text(
            "Cannot be eliminated even in free fall", font_size=20, color=RED_A
        )
        def2_group = VGroup(def2, def2_en).arrange(DOWN, buff=0.1)
        def2_group.next_to(arrow, DOWN, buff=0.3)

        self.play(Write(def2_group))
        self.wait(1)

        # 強調ボックス
        # Emphasis box
        all_defs = VGroup(def1_group, arrow, def2_group)
        box = SurroundingRectangle(all_defs, color=YELLOW, buff=0.3, corner_radius=0.1)
        self.play(Create(box))
        self.wait(0.5)

        # パート4：結論
        # Part 4: Conclusion
        conclusion = Text("消せない重力効果", font_size=36, color=YELLOW)
        conclusion_en = Text("The Inescapable Gravity", font_size=26, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.6)

        self.play(Write(conclusion_group))
        self.wait(2)


class TidalForceDefinitionSimple(Scene):
    """
    シンプル版：潮汐力 = 消せない重力効果
    Simple version: Tidal Force = Inescapable Gravity Effect
    """

    def construct(self):
        # 等号形式で表示
        # Display in equation format
        tidal = Text("潮汐力", font_size=42, color=YELLOW)
        equals = Text("＝", font_size=42)
        definition = Text("消せない重力効果", font_size=42, color=RED)

        equation = VGroup(tidal, equals, definition).arrange(RIGHT, buff=0.3)

        tidal_en = Text("Tidal Force", font_size=28, color=YELLOW_A)
        equals_en = Text("=", font_size=28)
        definition_en = Text("Inescapable Gravity", font_size=28, color=RED_A)

        equation_en = VGroup(tidal_en, equals_en, definition_en).arrange(RIGHT, buff=0.2)
        equation_en.next_to(equation, DOWN, buff=0.3)

        full_equation = VGroup(equation, equation_en)

        # アニメーション
        self.play(Write(tidal), Write(tidal_en))
        self.wait(0.3)
        self.play(Write(equals), Write(equals_en))
        self.wait(0.3)
        self.play(Write(definition), Write(definition_en))
        self.wait(0.5)

        # 強調
        box = SurroundingRectangle(
            full_equation, color=YELLOW, buff=0.4, corner_radius=0.15
        )
        self.play(Create(box))
        self.wait(0.5)

        # 補足テキスト
        note = Text("自由落下しても消すことができない", font_size=24, color=GRAY)
        note_en = Text(
            "Cannot be eliminated even in free fall", font_size=18, color=GRAY
        )
        note_group = VGroup(note, note_en).arrange(DOWN, buff=0.1)
        note_group.to_edge(DOWN, buff=0.8)

        self.play(Write(note_group))
        self.wait(2)


class TidalForceDefinitionVisual(Scene):
    """
    視覚的バージョン：球が変形して潮汐力を表現
    Visual version: Sphere deforms to represent tidal force
    """

    def construct(self):
        # タイトル
        title = Text("潮汐力の効果", font_size=28)
        title_en = Text("Effect of Tidal Force", font_size=20, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP)

        self.play(Write(title_group))
        self.wait(0.5)

        # 元の球
        original_ball = Circle(radius=1.0, color=BLUE, fill_opacity=0.6)
        original_ball.set_stroke(color=WHITE, width=3)

        self.play(GrowFromCenter(original_ball))
        self.wait(0.5)

        # 「重力が均一なら...」
        uniform_text = Text("均一な重力場では...", font_size=22)
        uniform_text_en = Text("In uniform gravity...", font_size=16, color=GRAY)
        uniform_group = VGroup(uniform_text, uniform_text_en).arrange(DOWN, buff=0.1)
        uniform_group.to_edge(DOWN, buff=1.0)

        self.play(Write(uniform_group))
        self.wait(0.5)

        # 球のまま落下（形は変わらない）
        no_change = Text("形は変わらない", font_size=20, color=GREEN)
        no_change_en = Text("Shape unchanged", font_size=14, color=GREEN_A)
        no_change_group = VGroup(no_change, no_change_en).arrange(DOWN, buff=0.05)
        no_change_group.next_to(original_ball, RIGHT, buff=0.5)

        self.play(FadeIn(no_change_group))
        self.wait(1)

        # テキストを更新
        self.play(FadeOut(no_change_group))

        nonuniform_text = Text("不均一な重力場では...", font_size=22, color=ORANGE)
        nonuniform_text_en = Text("In non-uniform gravity...", font_size=16, color=ORANGE)
        nonuniform_group = VGroup(nonuniform_text, nonuniform_text_en).arrange(
            DOWN, buff=0.1
        )
        nonuniform_group.to_edge(DOWN, buff=1.0)

        self.play(Transform(uniform_group, nonuniform_group))
        self.wait(0.5)

        # 球を楕円に変形（縦に伸び、横に縮む）
        ellipse = Ellipse(width=1.4, height=2.4, color=RED, fill_opacity=0.6)
        ellipse.set_stroke(color=WHITE, width=3)

        # 変形を示す矢印
        arrows = VGroup()
        # 上下に伸びる矢印
        up_arrow = Arrow(
            ellipse.get_top() + UP * 0.1,
            ellipse.get_top() + UP * 0.6,
            color=YELLOW,
            stroke_width=3,
        )
        down_arrow = Arrow(
            ellipse.get_bottom() + DOWN * 0.1,
            ellipse.get_bottom() + DOWN * 0.6,
            color=YELLOW,
            stroke_width=3,
        )
        # 左右に縮む矢印
        left_arrow = Arrow(
            ellipse.get_left() + LEFT * 0.5,
            ellipse.get_left() + LEFT * 0.1,
            color=YELLOW,
            stroke_width=3,
        )
        right_arrow = Arrow(
            ellipse.get_right() + RIGHT * 0.5,
            ellipse.get_right() + RIGHT * 0.1,
            color=YELLOW,
            stroke_width=3,
        )
        arrows.add(up_arrow, down_arrow, left_arrow, right_arrow)

        self.play(
            Transform(original_ball, ellipse),
            *[GrowArrow(arrow) for arrow in arrows],
            run_time=1.5,
        )
        self.wait(0.5)

        # 「縦に伸び、横に縮む」
        deform_text = Text("縦に伸び、横に縮む", font_size=22, color=YELLOW)
        deform_text_en = Text(
            "Stretched vertically, compressed horizontally", font_size=14, color=YELLOW_A
        )
        deform_group = VGroup(deform_text, deform_text_en).arrange(DOWN, buff=0.05)
        deform_group.next_to(original_ball, RIGHT, buff=0.8)

        self.play(Write(deform_group))
        self.wait(1)

        # 結論
        conclusion = Text("これが潮汐力", font_size=32, color=YELLOW)
        conclusion_en = Text("This is Tidal Force", font_size=24, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.5)

        self.play(
            FadeOut(uniform_group),
            Write(conclusion_group),
        )
        self.wait(2)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/tidal_force_definition.py TidalForceDefinition")
    print("  manim -pql scripts/tidal_force_definition.py TidalForceDefinitionSimple")
    print("  manim -pql scripts/tidal_force_definition.py TidalForceDefinitionVisual")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  TidalForceDefinition       - フル版：等価原理からの流れで潮汐力を定義")
    print("                               Full version: Define tidal force from equivalence principle")
    print("  TidalForceDefinitionSimple - シンプル版：潮汐力 = 消せない重力効果")
    print("                               Simple version: Tidal Force = Inescapable Gravity")
    print("  TidalForceDefinitionVisual - 視覚版：球が変形する様子で表現")
    print("                               Visual version: Show sphere deformation")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
