"""
潮汐力の比較アニメーション：横並び vs 縦並び
Tidal Force Comparison Animation: Horizontal vs Vertical alignment

左側：横に並べたボール → 近づく（収束）
右側：縦に並べたボール → 離れる（発散）

Left side: Horizontally aligned balls → converge
Right side: Vertically aligned balls → diverge

yt_script.md L107-110 の解説用
"""

from manim import *
import numpy as np


class TidalComparison(Scene):
    """
    2つのシナリオを横に並べて同時に表示するアニメーション
    Animation showing both scenarios side by side simultaneously
    """

    def construct(self):
        # 画面を左右に分割
        # Split screen into left and right

        # ===== タイトル =====
        # ===== Title =====
        title = Text("潮汐力：横並び vs 縦並び", font_size=28)
        title_en = Text("Tidal Force: Horizontal vs Vertical", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.5)

        # ===== 左側：横並びのボール（収束） =====
        # ===== Left side: Horizontal balls (converging) =====
        left_center = LEFT * 3.2 + DOWN * 0.5

        # 地球（左）
        earth_left = Circle(radius=1.5, color=BLUE, fill_opacity=0.25)
        earth_left.set_stroke(color=BLUE_B, width=3)
        earth_left.move_to(left_center)

        # 地球の中心点（左）
        center_dot_left = Dot(left_center, radius=0.06, color=WHITE)

        # ラベル（左）
        label_left = Text("横並び / Horizontal", font_size=16, color=YELLOW)
        label_left.next_to(earth_left, DOWN, buff=0.2)

        # ===== 右側：縦並びのボール（発散） =====
        # ===== Right side: Vertical balls (diverging) =====
        right_center = RIGHT * 3.2 + DOWN * 0.5

        # 地球（右）
        earth_right = Circle(radius=1.5, color=BLUE, fill_opacity=0.25)
        earth_right.set_stroke(color=BLUE_B, width=3)
        earth_right.move_to(right_center)

        # 地球の中心点（右）
        center_dot_right = Dot(right_center, radius=0.06, color=WHITE)

        # ラベル（右）
        label_right = Text("縦並び / Vertical", font_size=16, color=GREEN)
        label_right.next_to(earth_right, DOWN, buff=0.2)

        # 中央の区切り線
        # Center divider line
        divider = DashedLine(
            UP * 2.5 + DOWN * 0.5,
            DOWN * 3.5,
            color=GRAY,
            stroke_width=1,
            dash_length=0.15,
        )

        # 地球とラベルを表示
        # Display Earth and labels
        self.play(
            GrowFromCenter(earth_left),
            GrowFromCenter(earth_right),
            FadeIn(center_dot_left),
            FadeIn(center_dot_right),
            Create(divider),
            run_time=0.8,
        )
        self.play(
            Write(label_left),
            Write(label_right),
            run_time=0.5,
        )
        self.wait(0.3)

        # ===== ボールの設定 =====
        # ===== Ball settings =====
        ball_radius = 0.1
        start_height = 2.2  # 地球中心からの高さ

        # --- 左側：横並びのボール ---
        # --- Left side: Horizontal balls ---
        h_spacing = 0.8  # 横方向の間隔

        ball_h_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_left.set_stroke(color=WHITE, width=2)
        ball_h_left.move_to(left_center + LEFT * (h_spacing / 2) + UP * start_height)

        ball_h_right = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h_right.set_stroke(color=WHITE, width=2)
        ball_h_right.move_to(left_center + RIGHT * (h_spacing / 2) + UP * start_height)

        # --- 右側：縦並びのボール ---
        # --- Right side: Vertical balls ---
        v_spacing = 0.6  # 縦方向の間隔

        ball_v_lower = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v_lower.set_stroke(color=WHITE, width=2)
        ball_v_lower.move_to(right_center + UP * start_height)

        ball_v_upper = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v_upper.set_stroke(color=WHITE, width=2)
        ball_v_upper.move_to(right_center + UP * (start_height + v_spacing))

        # ボールを表示
        # Display balls
        self.play(
            FadeIn(ball_h_left, scale=0.5),
            FadeIn(ball_h_right, scale=0.5),
            FadeIn(ball_v_lower, scale=0.5),
            FadeIn(ball_v_upper, scale=0.5),
            run_time=0.6,
        )
        self.wait(0.3)

        # ===== 落下経路（点線） =====
        # ===== Fall trajectories (dashed lines) =====

        # 左側：中心に向かう経路
        trajectory_h_left = DashedLine(
            ball_h_left.get_center(),
            left_center,
            color=RED_A,
            stroke_width=1.5,
            dash_length=0.1,
            stroke_opacity=0.5,
        )
        trajectory_h_right = DashedLine(
            ball_h_right.get_center(),
            left_center,
            color=RED_A,
            stroke_width=1.5,
            dash_length=0.1,
            stroke_opacity=0.5,
        )

        # 右側：まっすぐ下向きの経路
        trajectory_v_lower = DashedLine(
            ball_v_lower.get_center(),
            right_center + UP * 0.3,
            color=GREEN_A,
            stroke_width=1.5,
            dash_length=0.1,
            stroke_opacity=0.5,
        )
        trajectory_v_upper = DashedLine(
            ball_v_upper.get_center(),
            right_center + UP * 1.4,
            color=GREEN_A,
            stroke_width=1.5,
            dash_length=0.1,
            stroke_opacity=0.5,
        )

        self.play(
            Create(trajectory_h_left),
            Create(trajectory_h_right),
            Create(trajectory_v_lower),
            Create(trajectory_v_upper),
            run_time=0.6,
        )
        self.wait(0.5)

        # ===== 落下アニメーション（同時に） =====
        # ===== Fall animation (simultaneously) =====
        fall_duration = 2.5

        # 左側：ボールが中心で衝突
        h_final = left_center

        # 右側：下のボールがより速く落ちる
        v_lower_final = right_center + UP * 0.3
        v_upper_final = right_center + UP * 1.4

        # 説明テキスト
        # Explanation text
        converge_text = Text("近づく→", font_size=18, color=YELLOW)
        converge_text.next_to(ball_h_left, LEFT, buff=0.3)

        diverge_text = Text("←離れる", font_size=18, color=GREEN)
        diverge_text.next_to(ball_v_upper, RIGHT, buff=0.3)

        self.play(
            # 左側：収束
            ball_h_left.animate.move_to(h_final),
            ball_h_right.animate.move_to(h_final),
            # 右側：発散
            ball_v_lower.animate.move_to(v_lower_final),
            ball_v_upper.animate.move_to(v_upper_final),
            # テキスト
            FadeIn(converge_text),
            FadeIn(diverge_text),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 左側：衝突エフェクト
        # Left side: Collision effect
        collision_flash = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        collision_flash.move_to(left_center)
        self.play(GrowFromCenter(collision_flash), run_time=0.15)
        self.play(
            collision_flash.animate.scale(2).set_opacity(0),
            run_time=0.25,
        )
        self.remove(collision_flash)

        # ===== 結論 =====
        # ===== Conclusion =====
        conclusion_left = Text("衝突！", font_size=20, color=YELLOW)
        conclusion_left.next_to(earth_left, UP, buff=0.1)

        conclusion_right = Text("離れた！", font_size=20, color=GREEN)
        conclusion_right.next_to(earth_right, UP, buff=0.1)

        self.play(
            Write(conclusion_left),
            Write(conclusion_right),
            FadeOut(converge_text),
            FadeOut(diverge_text),
        )
        self.wait(0.5)

        # 最終メッセージ
        # Final message
        final_text = Text(
            "これが「潮汐力」の正体！",
            font_size=24,
            color=WHITE,
        )
        final_text_en = Text(
            "This is the true nature of tidal force!",
            font_size=16,
            color=GRAY,
        )
        final_group = VGroup(final_text, final_text_en).arrange(DOWN, buff=0.1)
        final_group.to_edge(DOWN, buff=0.3)

        self.play(Write(final_group))
        self.wait(2)


class TidalComparisonSimple(Scene):
    """
    シンプル版：最小限の構成
    Simple version: Minimal configuration
    """

    def construct(self):
        # 左右の中心位置
        left_center = LEFT * 3 + DOWN * 0.3
        right_center = RIGHT * 3 + DOWN * 0.3

        # 地球
        earth_left = Circle(radius=1.3, color=BLUE, fill_opacity=0.2)
        earth_left.set_stroke(color=BLUE_B, width=2)
        earth_left.move_to(left_center)

        earth_right = Circle(radius=1.3, color=BLUE, fill_opacity=0.2)
        earth_right.set_stroke(color=BLUE_B, width=2)
        earth_right.move_to(right_center)

        center_dot_left = Dot(left_center, radius=0.05, color=WHITE)
        center_dot_right = Dot(right_center, radius=0.05, color=WHITE)

        # タイトルラベル
        label_left = Text("横 / Horizontal", font_size=14, color=YELLOW)
        label_left.next_to(earth_left, DOWN, buff=0.15)
        label_right = Text("縦 / Vertical", font_size=14, color=GREEN)
        label_right.next_to(earth_right, DOWN, buff=0.15)

        self.add(earth_left, earth_right, center_dot_left, center_dot_right)
        self.add(label_left, label_right)
        self.wait(0.3)

        # ボール設定
        ball_radius = 0.09
        start_height = 2.0

        # 左側ボール
        h_spacing = 0.7
        ball_h1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h1.set_stroke(color=WHITE, width=1.5)
        ball_h1.move_to(left_center + LEFT * (h_spacing / 2) + UP * start_height)

        ball_h2 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h2.set_stroke(color=WHITE, width=1.5)
        ball_h2.move_to(left_center + RIGHT * (h_spacing / 2) + UP * start_height)

        # 右側ボール
        v_spacing = 0.5
        ball_v1 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v1.set_stroke(color=WHITE, width=1.5)
        ball_v1.move_to(right_center + UP * start_height)

        ball_v2 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v2.set_stroke(color=WHITE, width=1.5)
        ball_v2.move_to(right_center + UP * (start_height + v_spacing))

        self.play(
            FadeIn(ball_h1, scale=0.5),
            FadeIn(ball_h2, scale=0.5),
            FadeIn(ball_v1, scale=0.5),
            FadeIn(ball_v2, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.5)

        # 落下アニメーション
        self.play(
            ball_h1.animate.move_to(left_center),
            ball_h2.animate.move_to(left_center),
            ball_v1.animate.move_to(right_center + UP * 0.3),
            ball_v2.animate.move_to(right_center + UP * 1.3),
            run_time=2.0,
            rate_func=rate_functions.ease_in_quad,
        )

        # 衝突フラッシュ（左側のみ）
        flash = Circle(radius=0.25, color=YELLOW, fill_opacity=0.8)
        flash.move_to(left_center)
        self.play(GrowFromCenter(flash), run_time=0.1)
        self.play(flash.animate.scale(2).set_opacity(0), run_time=0.2)
        self.remove(flash)

        self.wait(1.5)


class TidalComparisonWithArrows(Scene):
    """
    矢印付き版：重力の方向と強さを可視化
    Arrow version: Visualize gravity direction and strength
    """

    def construct(self):
        # タイトル
        title = Text("潮汐力の仕組み", font_size=28)
        title_en = Text("How Tidal Forces Work", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # 左右の中心位置
        left_center = LEFT * 3.2 + DOWN * 0.5
        right_center = RIGHT * 3.2 + DOWN * 0.5

        # 地球
        earth_left = Circle(radius=1.5, color=BLUE, fill_opacity=0.25)
        earth_left.set_stroke(color=BLUE_B, width=3)
        earth_left.move_to(left_center)

        earth_right = Circle(radius=1.5, color=BLUE, fill_opacity=0.25)
        earth_right.set_stroke(color=BLUE_B, width=3)
        earth_right.move_to(right_center)

        center_dot_left = Dot(left_center, radius=0.06, color=WHITE)
        center_dot_right = Dot(right_center, radius=0.06, color=WHITE)

        # ラベル
        label_left = Text("横並び", font_size=16, color=YELLOW)
        label_left.next_to(earth_left, DOWN, buff=0.2)
        label_right = Text("縦並び", font_size=16, color=GREEN)
        label_right.next_to(earth_right, DOWN, buff=0.2)

        # 区切り線
        divider = DashedLine(UP * 2.5, DOWN * 3.5, color=GRAY, stroke_width=1)

        self.play(
            GrowFromCenter(earth_left),
            GrowFromCenter(earth_right),
            FadeIn(center_dot_left),
            FadeIn(center_dot_right),
            Create(divider),
            Write(label_left),
            Write(label_right),
            run_time=0.8,
        )
        self.wait(0.3)

        # ボール設定
        ball_radius = 0.1
        start_height = 2.2

        # 左側ボール
        h_spacing = 0.9
        left_ball_pos = left_center + LEFT * (h_spacing / 2) + UP * start_height
        right_ball_pos = left_center + RIGHT * (h_spacing / 2) + UP * start_height

        ball_h1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h1.set_stroke(color=WHITE, width=2)
        ball_h1.move_to(left_ball_pos)

        ball_h2 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_h2.set_stroke(color=WHITE, width=2)
        ball_h2.move_to(right_ball_pos)

        # 右側ボール
        v_spacing = 0.6
        lower_ball_pos = right_center + UP * start_height
        upper_ball_pos = right_center + UP * (start_height + v_spacing)

        ball_v1 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v1.set_stroke(color=WHITE, width=2)
        ball_v1.move_to(lower_ball_pos)

        ball_v2 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        ball_v2.set_stroke(color=WHITE, width=2)
        ball_v2.move_to(upper_ball_pos)

        self.play(
            FadeIn(ball_h1, scale=0.5),
            FadeIn(ball_h2, scale=0.5),
            FadeIn(ball_v1, scale=0.5),
            FadeIn(ball_v2, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.3)

        # ===== 重力の矢印を表示 =====
        # ===== Show gravity arrows =====

        # 左側：中心に向かう矢印
        left_dir1 = (left_center - left_ball_pos) / np.linalg.norm(left_center - left_ball_pos)
        left_dir2 = (left_center - right_ball_pos) / np.linalg.norm(left_center - right_ball_pos)

        arrow_h1 = Arrow(
            left_ball_pos,
            left_ball_pos + left_dir1 * 0.7,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
        )
        arrow_h2 = Arrow(
            right_ball_pos,
            right_ball_pos + left_dir2 * 0.7,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
        )

        # 右側：下向きの矢印（長さが異なる）
        arrow_v1 = Arrow(
            lower_ball_pos,
            lower_ball_pos + DOWN * 0.9,
            color=ORANGE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        arrow_v2 = Arrow(
            upper_ball_pos,
            upper_ball_pos + DOWN * 0.6,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )

        # 左側説明
        explain_left = Text("斜めに引かれる", font_size=14, color=ORANGE)
        explain_left.next_to(arrow_h1, LEFT, buff=0.1)

        # 右側説明
        explain_right1 = Text("強い", font_size=12, color=ORANGE)
        explain_right1.next_to(arrow_v1, LEFT, buff=0.1)
        explain_right2 = Text("弱い", font_size=12, color=ORANGE)
        explain_right2.next_to(arrow_v2, LEFT, buff=0.1)

        self.play(
            GrowArrow(arrow_h1),
            GrowArrow(arrow_h2),
            GrowArrow(arrow_v1),
            GrowArrow(arrow_v2),
            FadeIn(explain_left),
            FadeIn(explain_right1),
            FadeIn(explain_right2),
        )
        self.wait(1.5)

        # 矢印と説明をフェードアウト
        self.play(
            FadeOut(arrow_h1),
            FadeOut(arrow_h2),
            FadeOut(arrow_v1),
            FadeOut(arrow_v2),
            FadeOut(explain_left),
            FadeOut(explain_right1),
            FadeOut(explain_right2),
        )

        # 落下アニメーション
        fall_duration = 2.5

        result_left = Text("→ 近づく", font_size=16, color=YELLOW)
        result_left.next_to(earth_left, UP, buff=0.1)
        result_right = Text("→ 離れる", font_size=16, color=GREEN)
        result_right.next_to(earth_right, UP, buff=0.1)

        self.play(
            ball_h1.animate.move_to(left_center),
            ball_h2.animate.move_to(left_center),
            ball_v1.animate.move_to(right_center + UP * 0.3),
            ball_v2.animate.move_to(right_center + UP * 1.3),
            FadeIn(result_left),
            FadeIn(result_right),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 衝突エフェクト
        flash = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        flash.move_to(left_center)
        self.play(GrowFromCenter(flash), run_time=0.15)
        self.play(flash.animate.scale(2).set_opacity(0), run_time=0.2)
        self.remove(flash)

        # 最終メッセージ
        final = Text("潮汐力 = 時空の曲がり", font_size=24, color=WHITE)
        final_en = Text("Tidal Force = Curvature of Spacetime", font_size=16, color=GRAY)
        final_group = VGroup(final, final_en).arrange(DOWN, buff=0.1)
        final_group.to_edge(DOWN, buff=0.3)

        self.play(Write(final_group))
        self.wait(2)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/tidal_comparison.py TidalComparison")
    print("  manim -pql scripts/tidal_comparison.py TidalComparisonSimple")
    print("  manim -pql scripts/tidal_comparison.py TidalComparisonWithArrows")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  TidalComparison          - 基本版（横並びと縦並びを比較）")
    print("                             Basic version (compare horizontal and vertical)")
    print("  TidalComparisonSimple    - シンプル版（最小構成）")
    print("                             Simple version (minimal)")
    print("  TidalComparisonWithArrows - 矢印付き版（重力の方向と強さを可視化）")
    print("                              Arrow version (visualize gravity direction and strength)")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
