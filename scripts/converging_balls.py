"""
横に並べた2つのボールが地球の中心で収束するアニメーション
Animation: Two horizontally aligned balls converge at Earth's center

地球は丸いので、重力は地球の「中心」に向かって働きます。
横に並んだ2つのボールは、それぞれ地球の中心に向かって落ちていくため、
落ちながら少しずつ近づいていき、最終的に地球の中心でぶつかります。

Since Earth is spherical, gravity points toward the center.
Two balls placed side by side will each fall toward the center,
gradually converging and eventually colliding at the center.
"""

from manim import *
import numpy as np


class ConvergingBalls(Scene):
    """
    横に並べた2つのボールが地球の中心で収束する様子を示すアニメーション
    Animation showing two horizontally aligned balls converging at Earth's center
    """

    def construct(self):
        # 地球を作成（透明度を持たせて内部が見えるように）
        # Create Earth (semi-transparent to show interior)
        earth_radius = 2.0
        earth_center = DOWN * 1.0  # 地球を下に移動 / Move Earth down
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
        ball_spacing = 1.2  # ボール間の距離 / Distance between balls
        start_height = 2.8  # 地球中心からの高さ / Height from Earth's center

        # 左のボール（赤）
        # Left ball (red)
        ball_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_left.set_stroke(color=WHITE, width=2)
        ball_left.move_to(earth_center + LEFT * (ball_spacing / 2) + UP * start_height)

        # 右のボール（青）
        # Right ball (blue)
        ball_right = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_right.set_stroke(color=WHITE, width=2)
        ball_right.move_to(earth_center + RIGHT * (ball_spacing / 2) + UP * start_height)

        # ボールを表示
        # Display balls
        self.play(
            GrowFromCenter(ball_left),
            GrowFromCenter(ball_right),
        )
        self.wait(0.3)

        # 重力の方向を示す矢印（地球の中心に向かう）
        # Gravity arrows pointing toward Earth's center
        left_pos = ball_left.get_center()
        right_pos = ball_right.get_center()

        # 矢印の方向を計算（中心に向かう）
        # Calculate arrow directions (toward center)
        left_direction = (earth_center - left_pos) / np.linalg.norm(earth_center - left_pos)
        right_direction = (earth_center - right_pos) / np.linalg.norm(earth_center - right_pos)

        arrow_length = 1.0
        gravity_left = Arrow(
            left_pos,
            left_pos + left_direction * arrow_length,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )
        gravity_right = Arrow(
            right_pos,
            right_pos + right_direction * arrow_length,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )

        # 説明テキスト
        # Explanation text
        text1 = Text(
            "重力は地球の「中心」に向かって働く",
            font_size=24,
        )
        text1_en = Text(
            "Gravity points toward Earth's center",
            font_size=18,
            color=GRAY,
        )
        text_group = VGroup(text1, text1_en).arrange(DOWN, buff=0.1)
        text_group.to_edge(UP)

        self.play(
            Write(text_group),
            GrowArrow(gravity_left),
            GrowArrow(gravity_right),
        )
        self.wait(1)

        # 矢印をフェードアウト
        # Fade out arrows
        self.play(
            FadeOut(gravity_left),
            FadeOut(gravity_right),
        )

        # 落下経路を点線で表示
        # Show fall trajectories as dashed lines
        trajectory_left = DashedLine(
            ball_left.get_center(),
            earth_center,
            color=RED_A,
            stroke_width=2,
            dash_length=0.15,
        )
        trajectory_right = DashedLine(
            ball_right.get_center(),
            earth_center,
            color=BLUE_A,
            stroke_width=2,
            dash_length=0.15,
        )

        self.play(
            Create(trajectory_left),
            Create(trajectory_right),
            run_time=0.8,
        )
        self.wait(0.5)

        # 説明テキストを更新
        # Update explanation text
        text2 = Text(
            "2つのボールは中心に向かって落ちていく",
            font_size=24,
        )
        text2_en = Text(
            "Both balls fall toward the center",
            font_size=18,
            color=GRAY,
        )
        text_group2 = VGroup(text2, text2_en).arrange(DOWN, buff=0.1)
        text_group2.to_edge(UP)

        self.play(Transform(text_group, text_group2))
        self.wait(0.5)

        # 落下アニメーション（中心に向かって加速）
        # Fall animation (accelerating toward center)
        fall_duration = 2.5

        self.play(
            ball_left.animate.move_to(earth_center),
            ball_right.animate.move_to(earth_center),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 衝突エフェクト
        # Collision effect
        collision_flash = Circle(radius=0.5, color=YELLOW, fill_opacity=0.8)
        collision_flash.move_to(earth_center)

        self.play(
            GrowFromCenter(collision_flash),
            run_time=0.2,
        )
        self.play(
            collision_flash.animate.scale(2).set_opacity(0),
            run_time=0.3,
        )
        self.remove(collision_flash)

        # 結論テキスト
        # Conclusion text
        conclusion = Text(
            "地球の中心でぶつかる！",
            font_size=28,
            color=YELLOW,
        )
        conclusion_en = Text(
            "They collide at Earth's center!",
            font_size=20,
            color=YELLOW_A,
        )
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(UP)

        self.play(Transform(text_group, conclusion_group))
        self.wait(2)


class ConvergingBallsSimple(Scene):
    """
    シンプル版：横に並べた2つのボールが収束
    Simple version: Two horizontally aligned balls converge
    """

    def construct(self):
        # 地球を作成
        # Create Earth
        earth_radius = 1.8
        earth_center = DOWN * 1.0  # 地球を下に移動 / Move Earth down
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
        ball_spacing = 1.1
        start_height = 2.8  # 地球中心からの高さ / Height from Earth's center

        # ボールを作成
        # Create balls
        ball_left = Circle(radius=ball_radius, color="#e74c3c", fill_opacity=0.9)
        ball_left.set_stroke(color=WHITE, width=2)
        ball_left.move_to(earth_center + LEFT * (ball_spacing / 2) + UP * start_height)

        ball_right = Circle(radius=ball_radius, color="#3498db", fill_opacity=0.9)
        ball_right.set_stroke(color=WHITE, width=2)
        ball_right.move_to(earth_center + RIGHT * (ball_spacing / 2) + UP * start_height)

        # 落下経路（点線）
        # Fall trajectories (dashed)
        trajectory_left = DashedLine(
            ball_left.get_center(),
            earth_center,
            color=RED_A,
            stroke_width=1.5,
            dash_length=0.12,
            stroke_opacity=0.6,
        )
        trajectory_right = DashedLine(
            ball_right.get_center(),
            earth_center,
            color=BLUE_A,
            stroke_width=1.5,
            dash_length=0.12,
            stroke_opacity=0.6,
        )

        # ボールと経路を表示
        # Display balls and trajectories
        self.play(
            FadeIn(ball_left, scale=0.5),
            FadeIn(ball_right, scale=0.5),
            Create(trajectory_left),
            Create(trajectory_right),
            run_time=0.8,
        )
        self.wait(0.5)

        # 落下アニメーション
        # Fall animation
        self.play(
            ball_left.animate.move_to(earth_center),
            ball_right.animate.move_to(earth_center),
            run_time=2.0,
            rate_func=rate_functions.ease_in_quad,
        )

        # 衝突フラッシュ
        # Collision flash
        flash = Circle(radius=0.3, color=YELLOW, fill_opacity=0.9)
        flash.move_to(earth_center)
        self.play(GrowFromCenter(flash), run_time=0.15)
        self.play(
            flash.animate.scale(2.5).set_opacity(0),
            run_time=0.25,
        )
        self.remove(flash)

        self.wait(1.5)


class ConvergingBallsWithLabels(Scene):
    """
    ラベル付き版：横に並べた2つのボールが収束
    Labeled version: Two horizontally aligned balls converge
    """

    def construct(self):
        # タイトル
        # Title
        title = Text("地球は丸い → 重力は中心に向かう", font_size=26)
        title_en = Text(
            "Earth is spherical → Gravity points to center",
            font_size=18,
            color=GRAY,
        )
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP)

        self.play(Write(title_group))
        self.wait(0.3)

        # 地球を作成
        # Create Earth
        earth_radius = 1.8
        center_pos = DOWN * 1.0  # 地球を下に移動 / Move Earth down
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
        ball_spacing = 1.1
        start_height = 2.8  # 地球中心からの高さ / Height from Earth's center

        # ボールを作成
        # Create balls
        ball_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball_left.set_stroke(color=WHITE, width=2)
        left_start = center_pos + LEFT * (ball_spacing / 2) + UP * start_height

        ball_right = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball_right.set_stroke(color=WHITE, width=2)
        right_start = center_pos + RIGHT * (ball_spacing / 2) + UP * start_height

        ball_left.move_to(left_start)
        ball_right.move_to(right_start)

        # ボール間の距離を示す矢印
        # Arrow showing distance between balls
        distance_arrow = DoubleArrow(
            left_start + DOWN * 0.4,
            right_start + DOWN * 0.4,
            color=YELLOW,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.08,
        )
        distance_label = Text("間隔 / Distance", font_size=14, color=YELLOW)
        distance_label.next_to(distance_arrow, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(ball_left),
            GrowFromCenter(ball_right),
        )
        self.play(
            GrowFromCenter(distance_arrow),
            FadeIn(distance_label),
        )
        self.wait(0.5)

        # 重力の方向を示す矢印
        # Gravity arrows
        left_dir = (center_pos - left_start) / np.linalg.norm(center_pos - left_start)
        right_dir = (center_pos - right_start) / np.linalg.norm(center_pos - right_start)

        gravity_left = Arrow(
            left_start,
            left_start + left_dir * 0.8,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
        )
        gravity_right = Arrow(
            right_start,
            right_start + right_dir * 0.8,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3,
        )

        self.play(
            GrowArrow(gravity_left),
            GrowArrow(gravity_right),
        )
        self.wait(0.5)

        # 矢印と距離表示をフェードアウト
        # Fade out arrows and distance display
        self.play(
            FadeOut(gravity_left),
            FadeOut(gravity_right),
            FadeOut(distance_arrow),
            FadeOut(distance_label),
        )

        # 落下経路（点線）
        # Fall trajectories (dashed)
        trajectory_left = DashedLine(
            left_start,
            center_pos,
            color=RED_A,
            stroke_width=2,
            dash_length=0.12,
            stroke_opacity=0.5,
        )
        trajectory_right = DashedLine(
            right_start,
            center_pos,
            color=BLUE_A,
            stroke_width=2,
            dash_length=0.12,
            stroke_opacity=0.5,
        )

        self.play(
            Create(trajectory_left),
            Create(trajectory_right),
            run_time=0.6,
        )

        # 落下アニメーション（距離が縮まる様子も表示）
        # Fall animation (showing decreasing distance)
        fall_duration = 2.5

        # 中間地点での距離を示すテキスト
        # Text showing decreasing distance
        shrinking_text = Text("間隔が縮まる...", font_size=20, color=YELLOW)
        shrinking_text_en = Text("Distance shrinking...", font_size=14, color=YELLOW_A)
        shrinking_group = VGroup(shrinking_text, shrinking_text_en).arrange(DOWN, buff=0.05)
        shrinking_group.to_edge(DOWN)

        self.play(
            ball_left.animate.move_to(center_pos),
            ball_right.animate.move_to(center_pos),
            FadeIn(shrinking_group),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # 衝突エフェクト
        # Collision effect
        self.play(FadeOut(shrinking_group), run_time=0.1)

        collision_flash = Circle(radius=0.4, color=YELLOW, fill_opacity=0.9)
        collision_flash.move_to(center_pos)
        self.play(GrowFromCenter(collision_flash), run_time=0.15)
        self.play(
            collision_flash.animate.scale(2).set_opacity(0),
            run_time=0.25,
        )
        self.remove(collision_flash)

        # 結論
        # Conclusion
        conclusion = Text("中心でぶつかる！", font_size=24, color=YELLOW)
        conclusion_en = Text("Collide at center!", font_size=16, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN)

        self.play(Write(conclusion_group))
        self.wait(2)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/converging_balls.py ConvergingBalls")
    print("  manim -pql scripts/converging_balls.py ConvergingBallsSimple")
    print("  manim -pql scripts/converging_balls.py ConvergingBallsWithLabels")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  ConvergingBalls       - 基本版（説明テキスト付き）")
    print("                          Basic version with explanation text")
    print("  ConvergingBallsSimple - シンプル版（最小構成）")
    print("                          Simple version (minimal)")
    print("  ConvergingBallsWithLabels - ラベル付き版（距離表示・重力矢印あり）")
    print("                              Labeled version with distance and gravity arrows")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
