"""
自由落下するエレベーター内で見る潮汐力のアニメーション
Animation: Tidal forces as seen from inside a free-falling elevator

落下中のエレベーターの中から見ると、ボールは「浮いている」ように見えます。
しかし、横に並べたボールは近づいていき、縦に並べたボールは離れていきます。
無重力のはずなのに、ボールが勝手に動いているように見える - これが潮汐力です。

From inside a free-falling elevator, balls appear to "float" in zero gravity.
However, horizontally aligned balls move closer together,
while vertically aligned balls move apart.
Despite apparent weightlessness, the balls seem to move on their own - this is tidal force.
"""

from manim import *


class TidalForceElevatorHorizontal(Scene):
    """
    エレベーター内で横に並べたボールが近づいていくアニメーション
    Animation: Horizontally aligned balls converging inside elevator
    """

    def construct(self):
        # エレベーターの箱を作成
        # Create elevator box
        elevator_width = 5.0
        elevator_height = 4.0
        elevator = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=4,
        )
        elevator.set_fill(color=GRAY_E, opacity=0.3)

        # エレベーターのドア（装飾）
        # Elevator door (decoration)
        door_gap = Line(
            elevator.get_center() + UP * (elevator_height / 2),
            elevator.get_center() + DOWN * (elevator_height / 2),
            color=GRAY_C,
            stroke_width=2,
        )

        # 落下を示す矢印（エレベーター外側）
        # Falling arrows (outside elevator)
        fall_arrows = VGroup()
        for x_offset in [-3.2, 3.2]:
            arrow = Arrow(
                UP * 1.5 + RIGHT * x_offset,
                DOWN * 1.5 + RIGHT * x_offset,
                color=YELLOW,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
            )
            fall_arrows.add(arrow)

        fall_label = Text("自由落下中", font_size=18, color=YELLOW)
        fall_label_en = Text("Free Falling", font_size=14, color=YELLOW_A)
        fall_label_group = VGroup(fall_label, fall_label_en).arrange(DOWN, buff=0.05)
        fall_label_group.to_edge(UP).shift(DOWN * 0.3)

        # シーンを表示
        # Display scene
        self.play(
            Create(elevator),
            Create(door_gap),
        )
        self.play(
            *[GrowArrow(arrow) for arrow in fall_arrows],
            Write(fall_label_group),
        )
        self.wait(0.5)

        # ボールを作成（横に並べる）
        # Create balls (horizontally aligned)
        ball_radius = 0.25
        ball_spacing = 2.0  # ボール間の初期距離 / Initial distance between balls

        ball_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_left.set_stroke(color=WHITE, width=2)
        ball_left.move_to(LEFT * (ball_spacing / 2))

        ball_right = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_right.set_stroke(color=WHITE, width=2)
        ball_right.move_to(RIGHT * (ball_spacing / 2))

        # ボールを表示
        # Display balls
        self.play(
            GrowFromCenter(ball_left),
            GrowFromCenter(ball_right),
        )
        self.wait(0.3)

        # 「浮いている」ことを示すテキスト
        # Text indicating floating
        floating_text = Text("ボールは浮いている（無重力）", font_size=22)
        floating_text_en = Text("Balls are floating (zero-G)", font_size=16, color=GRAY)
        floating_group = VGroup(floating_text, floating_text_en).arrange(DOWN, buff=0.1)
        floating_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Write(floating_group))
        self.wait(1)

        # テキストを更新
        # Update text
        approaching_text = Text("でも...少しずつ近づいていく", font_size=22, color=YELLOW)
        approaching_text_en = Text(
            "But...they slowly move closer", font_size=16, color=YELLOW_A
        )
        approaching_group = VGroup(approaching_text, approaching_text_en).arrange(
            DOWN, buff=0.1
        )
        approaching_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Transform(floating_group, approaching_group))

        # ボールが近づくアニメーション
        # Animation of balls approaching
        final_spacing = 0.8  # 最終的な距離 / Final distance

        self.play(
            ball_left.animate.move_to(LEFT * (final_spacing / 2)),
            ball_right.animate.move_to(RIGHT * (final_spacing / 2)),
            run_time=3.0,
            rate_func=rate_functions.linear,
        )

        # 結論テキスト
        # Conclusion text
        conclusion = Text("無重力なのに動く？", font_size=28, color=YELLOW)
        conclusion_en = Text("Moving in Zero-G?", font_size=20, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Transform(floating_group, conclusion_group))
        self.wait(2)


class TidalForceElevatorVertical(Scene):
    """
    エレベーター内で縦に並べたボールが離れていくアニメーション
    Animation: Vertically aligned balls diverging inside elevator
    """

    def construct(self):
        # エレベーターの箱を作成
        # Create elevator box
        elevator_width = 5.0
        elevator_height = 4.0
        elevator = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=4,
        )
        elevator.set_fill(color=GRAY_E, opacity=0.3)

        # エレベーターのドア（装飾）
        # Elevator door (decoration)
        door_gap = Line(
            elevator.get_center() + UP * (elevator_height / 2),
            elevator.get_center() + DOWN * (elevator_height / 2),
            color=GRAY_C,
            stroke_width=2,
        )

        # 落下を示す矢印（エレベーター外側）
        # Falling arrows (outside elevator)
        fall_arrows = VGroup()
        for x_offset in [-3.2, 3.2]:
            arrow = Arrow(
                UP * 1.5 + RIGHT * x_offset,
                DOWN * 1.5 + RIGHT * x_offset,
                color=YELLOW,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
            )
            fall_arrows.add(arrow)

        fall_label = Text("自由落下中", font_size=18, color=YELLOW)
        fall_label_en = Text("Free Falling", font_size=14, color=YELLOW_A)
        fall_label_group = VGroup(fall_label, fall_label_en).arrange(DOWN, buff=0.05)
        fall_label_group.to_edge(UP).shift(DOWN * 0.3)

        # シーンを表示
        # Display scene
        self.play(
            Create(elevator),
            Create(door_gap),
        )
        self.play(
            *[GrowArrow(arrow) for arrow in fall_arrows],
            Write(fall_label_group),
        )
        self.wait(0.5)

        # ボールを作成（縦に並べる）
        # Create balls (vertically aligned)
        ball_radius = 0.25
        ball_spacing = 1.0  # ボール間の初期距離 / Initial distance between balls

        ball_upper = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_upper.set_stroke(color=WHITE, width=2)
        ball_upper.move_to(UP * (ball_spacing / 2))

        ball_lower = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_lower.set_stroke(color=WHITE, width=2)
        ball_lower.move_to(DOWN * (ball_spacing / 2))

        # ボールを表示
        # Display balls
        self.play(
            GrowFromCenter(ball_upper),
            GrowFromCenter(ball_lower),
        )
        self.wait(0.3)

        # 「浮いている」ことを示すテキスト
        # Text indicating floating
        floating_text = Text("ボールは浮いている（無重力）", font_size=22)
        floating_text_en = Text("Balls are floating (zero-G)", font_size=16, color=GRAY)
        floating_group = VGroup(floating_text, floating_text_en).arrange(DOWN, buff=0.1)
        floating_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Write(floating_group))
        self.wait(1)

        # テキストを更新
        # Update text
        separating_text = Text("でも...少しずつ離れていく", font_size=22, color=GREEN)
        separating_text_en = Text(
            "But...they slowly move apart", font_size=16, color=GREEN_A
        )
        separating_group = VGroup(separating_text, separating_text_en).arrange(
            DOWN, buff=0.1
        )
        separating_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Transform(floating_group, separating_group))

        # ボールが離れるアニメーション（下のボールが下に動く）
        # Animation of balls separating (lower ball moves down)
        # 下のボールの方が強い重力を受けるので、下に動いていくように見える
        # The lower ball experiences stronger gravity, so it appears to move downward
        lower_final_y = -1.5  # 下のボールの最終位置 / Final position of lower ball

        self.play(
            ball_lower.animate.move_to(DOWN * abs(lower_final_y)),
            run_time=3.0,
            rate_func=rate_functions.linear,
        )

        # 結論テキスト
        # Conclusion text
        conclusion = Text("無重力なのに動く？", font_size=28, color=GREEN)
        conclusion_en = Text("Moving in Zero-G?", font_size=20, color=GREEN_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Transform(floating_group, conclusion_group))
        self.wait(2)


class TidalForceElevatorSideBySide(Scene):
    """
    2つのエレベーターを横に並べて表示：左は横並びボール、右は縦並びボール
    Animation: Two elevators side by side - left with horizontal balls, right with vertical balls
    """

    def construct(self):
        # 2つのエレベーターの設定
        # Settings for two elevators
        elevator_width = 3.0
        elevator_height = 4.0
        elevator_spacing = 0.8  # エレベーター間の隙間 / Gap between elevators

        # 左のエレベーター（横並びボール用）
        # Left elevator (for horizontal balls)
        left_center = LEFT * (elevator_width / 2 + elevator_spacing / 2)
        elevator_left = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=3,
        )
        elevator_left.set_fill(color=GRAY_E, opacity=0.3)
        elevator_left.move_to(left_center)

        # 右のエレベーター（縦並びボール用）
        # Right elevator (for vertical balls)
        right_center = RIGHT * (elevator_width / 2 + elevator_spacing / 2)
        elevator_right = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY_B,
            stroke_width=3,
        )
        elevator_right.set_fill(color=GRAY_E, opacity=0.3)
        elevator_right.move_to(right_center)

        # 落下を示す矢印（両エレベーターの外側）
        # Falling arrows (outside both elevators)
        fall_arrows = VGroup()
        for x_offset in [-4.0, 4.0]:
            arrow = Arrow(
                UP * 1.5 + RIGHT * x_offset,
                DOWN * 1.5 + RIGHT * x_offset,
                color=YELLOW,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
            )
            fall_arrows.add(arrow)

        fall_label = Text("自由落下中", font_size=18, color=YELLOW)
        fall_label_en = Text("Free Falling", font_size=14, color=YELLOW_A)
        fall_label_group = VGroup(fall_label, fall_label_en).arrange(DOWN, buff=0.05)
        fall_label_group.to_edge(UP).shift(DOWN * 0.2)

        # シーンを表示
        # Display scene
        self.play(
            Create(elevator_left),
            Create(elevator_right),
        )
        self.play(
            *[GrowArrow(arrow) for arrow in fall_arrows],
            Write(fall_label_group),
        )
        self.wait(0.5)

        # ボールの設定
        # Ball settings
        ball_radius = 0.2

        # 左のエレベーター：横に並べたボール
        # Left elevator: horizontally aligned balls
        h_spacing = 1.4  # 初期間隔 / Initial spacing
        ball_h_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_left.set_stroke(color=WHITE, width=2)
        ball_h_left.move_to(left_center + LEFT * (h_spacing / 2))

        ball_h_right = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_right.set_stroke(color=WHITE, width=2)
        ball_h_right.move_to(left_center + RIGHT * (h_spacing / 2))

        # 右のエレベーター：縦に並べたボール
        # Right elevator: vertically aligned balls
        v_spacing = 1.0  # 初期間隔 / Initial spacing
        ball_v_upper = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_v_upper.set_stroke(color=WHITE, width=2)
        ball_v_upper.move_to(right_center + UP * (v_spacing / 2))

        ball_v_lower = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_v_lower.set_stroke(color=WHITE, width=2)
        ball_v_lower.move_to(right_center + DOWN * (v_spacing / 2))

        # ボールを表示
        # Display balls
        self.play(
            GrowFromCenter(ball_h_left),
            GrowFromCenter(ball_h_right),
            GrowFromCenter(ball_v_upper),
            GrowFromCenter(ball_v_lower),
        )
        self.wait(0.5)

        # テキスト表示
        # Display text
        text = Text("無重力で浮いているはずなのに...", font_size=22)
        text_en = Text(
            "They should be floating in zero-G, but...", font_size=16, color=GRAY
        )
        text_group = VGroup(text, text_en).arrange(DOWN, buff=0.1)
        text_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Write(text_group))
        self.wait(1)

        # ボールが動くアニメーション
        # Animation of balls moving
        # 横：両方が中央に近づく
        # Horizontal: both move toward center
        h_final_spacing = 0.5

        # 縦：上のボールは静止、下のボールが下に動く
        # Vertical: upper ball stays, lower ball moves down
        # 下のボールの方が強い重力を受けるため
        # Because the lower ball experiences stronger gravity
        v_lower_final_y = -1.3

        self.play(
            ball_h_left.animate.move_to(left_center + LEFT * (h_final_spacing / 2)),
            ball_h_right.animate.move_to(left_center + RIGHT * (h_final_spacing / 2)),
            ball_v_lower.animate.move_to(right_center + DOWN * abs(v_lower_final_y)),
            run_time=3.0,
            rate_func=rate_functions.linear,
        )

        # 結果を示すラベル
        # Labels showing results
        converge_label = Text("近づく", font_size=18, color=RED_C)
        converge_label_en = Text("Converge", font_size=14, color=RED_A)
        converge_group = VGroup(converge_label, converge_label_en).arrange(DOWN, buff=0.05)
        converge_group.next_to(elevator_left, UP, buff=0.2)

        diverge_label = Text("離れる", font_size=18, color=BLUE_C)
        diverge_label_en = Text("Diverge", font_size=14, color=BLUE_A)
        diverge_group = VGroup(diverge_label, diverge_label_en).arrange(DOWN, buff=0.05)
        diverge_group.next_to(elevator_right, UP, buff=0.2)

        self.play(
            Write(converge_group),
            Write(diverge_group),
        )
        self.wait(1)

        # 最終メッセージ
        # Final message
        final_text = Text("無重力なのに動く？", font_size=28, color=YELLOW)
        final_text_en = Text("Moving in Zero-G?", font_size=20, color=YELLOW_A)
        final_group = VGroup(final_text, final_text_en).arrange(DOWN, buff=0.1)
        final_group.to_edge(DOWN).shift(UP * 0.3)

        self.play(Transform(text_group, final_group))
        self.wait(2)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/tidal_force_elevator.py TidalForceElevatorHorizontal")
    print("  manim -pql scripts/tidal_force_elevator.py TidalForceElevatorVertical")
    print("  manim -pql scripts/tidal_force_elevator.py TidalForceElevatorSideBySide")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  TidalForceElevatorHorizontal - 横に並べたボールが近づく（1つのエレベーター）")
    print("                                 Horizontally aligned balls converge (single elevator)")
    print("  TidalForceElevatorVertical   - 縦に並べたボールが離れる（1つのエレベーター）")
    print("                                 Vertically aligned balls diverge (single elevator)")
    print("  TidalForceElevatorSideBySide - 2つのエレベーターを横に並べて比較（推奨）")
    print("                                 Two elevators side by side comparison (recommended)")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
