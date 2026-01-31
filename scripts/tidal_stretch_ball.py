"""
ボールが潮汐力で引き伸ばされるアニメーション
Ball being stretched by tidal forces

円形のボールが地球の潮汐力によって縦長の楕円に変形する様子を示す。
8箇所（上下左右＋斜め4方向）に潮汐力の矢印を配置。

脚本L104-105に対応：
「さて、ここからが今日の本題です。」
「この潮汐力が「時空の曲がり」そのものだという話をしましょう。」
"""

from manim import *
import numpy as np


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


def calculate_gravity_direction_and_strength(point_pos, earth_center_pos):
    """
    各点での重力の方向と相対的な強さを計算する
    Calculate gravity direction and relative strength at each point

    重力は中心力なので、各点から地球中心に向かうベクトルになる。
    強さは距離の2乗に反比例する。
    （docs/chapter5.pdf Figure 5.1 右図参照）

    Args:
        point_pos: ボール表面上の点の位置 [x, y]
        earth_center_pos: 地球中心の位置 [x, y]

    Returns:
        (direction_x, direction_y, relative_strength)
        - direction: 正規化された重力方向ベクトル
        - relative_strength: 相対的な重力の強さ（基準点との比）
    """
    # 地球中心への方向ベクトル
    to_earth = np.array(earth_center_pos) - np.array(point_pos)
    distance = np.linalg.norm(to_earth)

    # 正規化
    direction = to_earth / distance

    # 相対的な強さ（距離の2乗に反比例、基準距離で正規化）
    base_distance = abs(earth_center_pos[1])  # 地球中心までの基準距離
    relative_strength = (base_distance / distance) ** 2

    return direction[0], direction[1], relative_strength


class TidalStretchBall(Scene):
    """潮汐力によるボールの変形 / Ball deformation due to tidal forces"""

    def construct(self):
        # 背景色を設定
        # Set background color
        self.camera.background_color = "#1a1a2e"

        # ボールの半径と位置
        # Ball radius and position
        ball_radius = 1.5
        ball_center = UP * 0.5

        # 円形のボールを作成
        # Create circular ball
        ball = Circle(
            radius=ball_radius,
            color=WHITE,
            fill_color="#4a90d9",
            fill_opacity=0.8,
            stroke_width=3,
        )
        ball.move_to(ball_center)

        # 地球を示す弧（画面下部）
        # Arc representing Earth (bottom of screen)
        earth_arc = Arc(
            radius=12,
            start_angle=PI * 0.4,
            angle=PI * 0.2,
            color="#3498db",
            stroke_width=10,
        )
        earth_arc.move_to(DOWN * 10)

        # 地球のラベル（バックプレート付き）
        # Earth label (with backplate)
        earth_label = create_text_with_backplate(
            "↓ 地球 / Earth ↓", font_size=22, text_color="#3498db"
        )
        earth_label.move_to(DOWN * 3.3)

        # --- フェーズ1: ボールと地球を表示 ---
        # --- Phase 1: Show ball and Earth ---
        self.play(
            FadeIn(ball, scale=0.8),
            run_time=0.8,
        )
        self.play(
            Create(earth_arc),
            FadeIn(earth_label),
            run_time=0.6,
        )
        self.wait(0.5)

        # --- フェーズ2: 8方向の重力矢印を作成 ---
        # --- Phase 2: Create gravity arrows in 8 directions ---
        # 全ての矢印が地球中心を向く（Figure 5.1 右図参照）
        # All arrows point toward Earth's center (see Figure 5.1 right)

        # 地球中心の位置（視覚的に矢印の収束がわかる程度に近く）
        # Earth's center position (close enough to show arrow convergence visually)
        earth_center = np.array([0, -8, 0])

        # 矢印のパラメータ
        # Arrow parameters
        base_arrow_length = 0.9
        arrow_start_gap = 0.15  # ボール表面からの開始ギャップ（外側に）

        # 8方向の角度（度数法）: 上、右上、右、右下、下、左下、左、左上
        # 8 directions (degrees): up, upper-right, right, lower-right, down, lower-left, left, upper-left
        angles = [90, 45, 0, 315, 270, 225, 180, 135]

        arrows = []

        for angle in angles:
            # ボール表面上の位置を計算
            # Calculate position on ball surface
            angle_rad = np.radians(angle)
            # ボール中心から見た外向き方向
            outward_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            surface_pos = ball_center + ball_radius * outward_dir

            # 重力の方向と強さを計算（地球中心に向かう）
            # Calculate gravity direction and strength (toward Earth's center)
            gx, gy, strength = calculate_gravity_direction_and_strength(
                surface_pos[:2], earth_center[:2]
            )
            gravity_dir = np.array([gx, gy, 0])

            # 矢印の長さは重力の強さに比例（視覚的に誇張、ただし常に正の値を保証）
            # Arrow length proportional to gravity strength (visually exaggerated, always positive)
            length_factor = max(0.4, 1.0 + (strength - 1.0) * 3)
            arrow_length = base_arrow_length * length_factor

            # 矢印の開始点：ボール表面から外側にギャップを取る
            # Arrow start: gap outward from ball surface
            start_pos = surface_pos + arrow_start_gap * outward_dir
            # 矢印の終了点：開始点から地球中心方向へ
            # Arrow end: from start toward Earth's center
            end_pos = start_pos + arrow_length * gravity_dir

            # 色は黄色で統一（重力ベクトルを表す）
            # Unified yellow color (representing gravity vectors)
            arrow = Arrow(
                start=start_pos,
                end=end_pos,
                color=YELLOW,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.3,
                buff=0,
            )
            arrows.append(arrow)

        # 説明テキスト
        # Explanation text
        explanation_jp = create_text_with_backplate(
            "重力は地球の中心を向く",
            font_size=24,
            text_color=WHITE,
            bg_opacity=0.85,
        )
        explanation_jp.move_to(RIGHT * 4.0 + UP * 2.5)

        explanation_en = create_text_with_backplate(
            "Gravity points to Earth's center",
            font_size=18,
            text_color=GRAY_B,
            bg_opacity=0.85,
        )
        explanation_en.next_to(explanation_jp, DOWN, buff=0.2)

        # 凡例：重力の強さの違い
        # Legend: Gravity strength difference
        legend_strong = create_text_with_backplate(
            "下側: 地球に近い → 重力強い",
            font_size=18,
            text_color=ORANGE,
            bg_opacity=0.8,
        )
        legend_strong.move_to(RIGHT * 4.0 + UP * 1.0)

        legend_strong_en = create_text_with_backplate(
            "Bottom: Closer → Stronger gravity",
            font_size=16,
            text_color=GRAY_B,
            bg_opacity=0.8,
        )
        legend_strong_en.next_to(legend_strong, DOWN, buff=0.15)

        legend_weak = create_text_with_backplate(
            "上側: 地球から遠い → 重力弱い",
            font_size=18,
            text_color=YELLOW,
            bg_opacity=0.8,
        )
        legend_weak.next_to(legend_strong_en, DOWN, buff=0.3)

        legend_weak_en = create_text_with_backplate(
            "Top: Farther → Weaker gravity",
            font_size=16,
            text_color=GRAY_B,
            bg_opacity=0.8,
        )
        legend_weak_en.next_to(legend_weak, DOWN, buff=0.15)

        # 全ての矢印を一度に表示
        # Show all arrows at once
        self.play(
            FadeIn(explanation_jp),
            FadeIn(explanation_en),
            run_time=0.5,
        )

        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            run_time=0.8,
        )

        self.play(
            FadeIn(legend_strong),
            FadeIn(legend_strong_en),
            FadeIn(legend_weak),
            FadeIn(legend_weak_en),
            run_time=0.6,
        )
        self.wait(0.8)

        # --- フェーズ3: ボールを楕円に変形 ---
        # --- Phase 3: Deform ball into ellipse ---

        deform_label = create_text_with_backplate(
            "重力の差でボールが変形",
            font_size=20,
            text_color=WHITE,
            bg_opacity=0.85,
        )
        deform_label.move_to(RIGHT * 4.0 + DOWN * 1.2)

        deform_label_en = create_text_with_backplate(
            "Ball deforms due to gravity difference",
            font_size=16,
            text_color=GRAY_B,
            bg_opacity=0.85,
        )
        deform_label_en.next_to(deform_label, DOWN, buff=0.15)

        self.play(FadeIn(deform_label), FadeIn(deform_label_en), run_time=0.4)

        # 変形量
        # Deformation amount
        stretch_factor = 1.22  # 縦方向に22%伸びる
        compress_factor = 0.83  # 横方向に17%縮む

        # 矢印も一緒に動かす（常に地球中心を向くように）
        # Move arrows along with deformation (always pointing to Earth's center)
        def create_arrow_animations():
            """矢印の移動アニメーションを生成"""
            anims = []
            for i, angle in enumerate(angles):
                angle_rad = np.radians(angle)
                # 変形後の位置を計算
                # Calculate position after deformation
                # 楕円上の点: (a*cosθ, b*sinθ) where a=compress, b=stretch
                new_surface_x = ball_center[0] + ball_radius * compress_factor * np.cos(angle_rad)
                new_surface_y = ball_center[1] + ball_radius * stretch_factor * np.sin(angle_rad)
                new_surface_pos = np.array([new_surface_x, new_surface_y, 0])

                # 楕円の外向き方向（近似的に元の角度方向）
                outward_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])

                # 重力方向を再計算（地球中心に向かう）
                gx, gy, strength = calculate_gravity_direction_and_strength(
                    new_surface_pos[:2], earth_center[:2]
                )
                gravity_dir = np.array([gx, gy, 0])

                # 矢印の長さも更新（常に正の値を保証）
                length_factor = max(0.4, 1.0 + (strength - 1.0) * 3)
                new_arrow_length = base_arrow_length * length_factor

                # 開始点：表面から外側にギャップ
                new_start = new_surface_pos + arrow_start_gap * outward_dir
                # 終了点：地球中心方向へ
                new_end = new_start + new_arrow_length * gravity_dir

                # 矢印を新しい位置に移動
                anims.append(arrows[i].animate.put_start_and_end_on(new_start, new_end))
            return anims

        self.play(
            ball.animate.stretch(stretch_factor, dim=1).stretch(compress_factor, dim=0),
            *create_arrow_animations(),
            run_time=1.2,
            rate_func=rate_functions.ease_out_quad,
        )

        self.wait(0.5)

        # --- フェーズ4: 潮汐力ラベルを強調 ---
        # --- Phase 4: Emphasize tidal force label ---

        tidal_label = create_text_with_backplate(
            "これが「潮汐力」",
            font_size=28,
            text_color=YELLOW,
            bg_opacity=0.9,
        )
        tidal_label.move_to(RIGHT * 4.0 + DOWN * 2.5)

        tidal_label_en = create_text_with_backplate(
            "This is the \"Tidal Force\"",
            font_size=22,
            text_color=YELLOW,
            bg_opacity=0.9,
        )
        tidal_label_en.next_to(tidal_label, DOWN, buff=0.15)

        self.play(FadeIn(tidal_label), FadeIn(tidal_label_en), run_time=0.6)

        # 強調アニメーション
        # Emphasis animation
        tidal_group = VGroup(tidal_label, tidal_label_en)
        self.play(
            tidal_group.animate.scale(1.1),
            run_time=0.25,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            tidal_group.animate.scale(1 / 1.1),
            run_time=0.25,
            rate_func=rate_functions.ease_in_quad,
        )

        self.wait(2.0)


class TidalStretchBallSimple(Scene):
    """シンプル版：潮汐力によるボールの変形 / Simple version: Ball deformation due to tidal forces"""

    def construct(self):
        # 背景色
        self.camera.background_color = "#1a1a2e"

        # ボール
        ball_radius = 1.8
        ball_center = ORIGIN
        ball = Circle(
            radius=ball_radius,
            color=WHITE,
            fill_color="#4a90d9",
            fill_opacity=0.8,
            stroke_width=3,
        )
        ball.move_to(ball_center)

        # 地球の弧
        earth_arc = Arc(
            radius=12,
            start_angle=PI * 0.4,
            angle=PI * 0.2,
            color="#3498db",
            stroke_width=8,
        )
        earth_arc.move_to(DOWN * 10.5)

        self.play(FadeIn(ball, scale=0.8), Create(earth_arc), run_time=0.7)
        self.wait(0.3)

        # 地球中心の位置（視覚的に矢印の収束がわかる程度に近く）
        earth_center = np.array([0, -8, 0])

        # 8方向の矢印を一度に作成・表示（全て地球中心を向く）
        base_arrow_length = 0.8
        arrow_start_gap = 0.15
        angles = [90, 45, 0, 315, 270, 225, 180, 135]

        arrows = []
        for angle in angles:
            angle_rad = np.radians(angle)
            outward_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
            surface_pos = ball_center + ball_radius * outward_dir

            # 重力方向と強さを計算
            gx, gy, strength = calculate_gravity_direction_and_strength(
                surface_pos[:2], earth_center[:2]
            )
            gravity_dir = np.array([gx, gy, 0])

            # 矢印の長さは重力の強さに比例（常に正の値を保証）
            length_factor = max(0.4, 1.0 + (strength - 1.0) * 3)
            arrow_length = base_arrow_length * length_factor

            # 開始点：表面から外側にギャップ
            start_pos = surface_pos + arrow_start_gap * outward_dir
            # 終了点：地球中心方向へ
            end_pos = start_pos + arrow_length * gravity_dir

            arrow = Arrow(
                start=start_pos,
                end=end_pos,
                color=YELLOW,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.3,
                buff=0,
            )
            arrows.append(arrow)

        self.play(*[GrowArrow(a) for a in arrows], run_time=0.6)
        self.wait(0.4)

        # 変形
        stretch_factor = 1.25
        compress_factor = 0.82

        def create_arrow_animations():
            anims = []
            for i, angle in enumerate(angles):
                angle_rad = np.radians(angle)
                new_x = ball_center[0] + ball_radius * compress_factor * np.cos(angle_rad)
                new_y = ball_center[1] + ball_radius * stretch_factor * np.sin(angle_rad)
                new_surface_pos = np.array([new_x, new_y, 0])

                # 外向き方向
                outward_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])

                # 重力方向を再計算
                gx, gy, strength = calculate_gravity_direction_and_strength(
                    new_surface_pos[:2], earth_center[:2]
                )
                gravity_dir = np.array([gx, gy, 0])

                length_factor = max(0.4, 1.0 + (strength - 1.0) * 3)
                new_arrow_length = base_arrow_length * length_factor

                new_start = new_surface_pos + arrow_start_gap * outward_dir
                new_end = new_start + new_arrow_length * gravity_dir
                anims.append(arrows[i].animate.put_start_and_end_on(new_start, new_end))
            return anims

        self.play(
            ball.animate.stretch(stretch_factor, dim=1).stretch(compress_factor, dim=0),
            *create_arrow_animations(),
            run_time=1.0,
            rate_func=rate_functions.ease_out_quad,
        )

        # ラベル
        tidal_label = create_text_with_backplate(
            "潮汐力 / Tidal Force",
            font_size=32,
            text_color=YELLOW,
            bg_opacity=0.85,
        )
        tidal_label.move_to(DOWN * 3.0)

        self.play(FadeIn(tidal_label), run_time=0.5)
        self.wait(1.5)


if __name__ == "__main__":
    print("使用方法:")
    print("  manim -pql scripts/tidal_stretch_ball.py TidalStretchBall")
    print("  manim -pql scripts/tidal_stretch_ball.py TidalStretchBallSimple")
    print("")
    print("シーン説明:")
    print("  TidalStretchBall       - 詳細版（段階的に矢印を表示、凡例付き）")
    print("  TidalStretchBallSimple - シンプル版（短縮バージョン）")
    print("")
    print("脚本L104-105に対応:")
    print("  「さて、ここからが今日の本題です。」")
    print("  「この潮汐力が「時空の曲がり」そのものだという話をしましょう。」")
