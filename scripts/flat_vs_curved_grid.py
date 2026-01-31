"""
平坦な空間 vs 曲がった空間（格子の対比）
Flat Space vs Curved Space (Grid Comparison)

左側：平坦な空間（正方形の格子）- 平行線は交わらない
右側：曲がった空間（モルワイデ図法風）- 経線が極で交わる

Left: Flat space (square grid) - Parallel lines never meet
Right: Curved space (Mollweide-style) - Meridians converge at poles

yt_script.md L112-118 の解説用
後の平行移動（L154-173）への伏線も兼ねる
"""

from manim import *
import numpy as np


class FlatVsCurvedGrid(Scene):
    """
    平坦な空間と曲がった空間（モルワイデ図法風）の格子を比較
    Compare flat space grid with curved space (Mollweide-style) grid
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("平坦な空間 vs 曲がった空間", font_size=28)
        title_en = Text("Flat Space vs Curved Space", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # ===== 左側：平坦な格子 =====
        left_center = LEFT * 3.3

        flat_grid = self.create_flat_grid()
        flat_grid.move_to(left_center)

        flat_label = Text("平坦 / Flat", font_size=18, color=YELLOW)
        flat_label.next_to(flat_grid, DOWN, buff=0.3)

        # ===== 右側：モルワイデ図法風の格子 =====
        right_center = RIGHT * 3.3

        curved_grid = self.create_mollweide_grid()
        curved_grid.move_to(right_center)

        curved_label = Text("曲がった / Curved", font_size=18, color=GREEN)
        curved_label.next_to(curved_grid, DOWN, buff=0.3)

        # 区切り線
        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1)

        # 格子を表示
        self.play(
            Create(flat_grid),
            Create(curved_grid),
            Create(divider),
            run_time=1.5,
        )
        self.play(
            Write(flat_label),
            Write(curved_label),
            run_time=0.5,
        )
        self.wait(0.5)

        # ===== ボールを配置 =====
        ball_radius = 0.1

        # モルワイデ図法のパラメータ（create_mollweide_gridと同じ）
        a = 2.0  # 横幅
        b = 1.7  # 縦幅

        # 格子のパラメータ（create_flat_gridと同じ）
        grid_size = 1.8
        # 格子線の間隔: 5本の線で間隔は0.9
        # 左から2番目の線: x = -0.9, 右から2番目の線: x = 0.9
        grid_line_x = 0.9

        # 左側：格子線に沿って落ちるボール（上端から開始）
        flat_ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        flat_ball1.set_stroke(color=WHITE, width=2)
        flat_ball1.move_to(left_center + LEFT * grid_line_x + UP * grid_size)

        flat_ball2 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        flat_ball2.set_stroke(color=WHITE, width=2)
        flat_ball2.move_to(left_center + RIGHT * grid_line_x + UP * grid_size)

        # 右側：北極点からスタート（経線に沿って移動）
        # 2つの経線のパラメータ（左右対称）
        t1 = -0.3  # 左側の経線
        t2 = 0.3   # 右側の経線

        # 北極点の位置
        north_pole = right_center + UP * b

        curved_ball1 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        curved_ball1.set_stroke(color=WHITE, width=2)
        curved_ball1.move_to(north_pole)  # 北極からスタート

        curved_ball2 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        curved_ball2.set_stroke(color=WHITE, width=2)
        curved_ball2.move_to(north_pole)  # 北極からスタート

        self.play(
            FadeIn(flat_ball1, scale=0.5),
            FadeIn(flat_ball2, scale=0.5),
            FadeIn(curved_ball1, scale=0.5),
            FadeIn(curved_ball2, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.3)

        # ===== 「まっすぐ進む」テキスト =====
        straight_text = Text("まっすぐ進む", font_size=16, color=WHITE)
        straight_text_en = Text("Moving straight", font_size=12, color=GRAY)
        straight_group = VGroup(straight_text, straight_text_en).arrange(DOWN, buff=0.05)
        straight_group.next_to(title_group, DOWN, buff=0.2)

        self.play(Write(straight_group), run_time=0.5)
        self.wait(0.3)

        # ===== 落下アニメーション =====
        fall_duration = 2.0

        # 左側：格子線に沿って平行のまま落下
        flat_final1 = left_center + LEFT * grid_line_x + DOWN * grid_size
        flat_final2 = left_center + RIGHT * grid_line_x + DOWN * grid_size

        # 南極点の位置
        south_pole = right_center + DOWN * b

        # 右側：経線に沿った移動（UpdateFromAlphaFuncを使用）
        def create_meridian_updater(center, a_val, b_val, t_val):
            """経線に沿ってボールを移動させるアップデータを作成"""
            def updater(mob, alpha):
                # alpha: 0 -> 1 に対して theta: PI/2 -> -PI/2
                theta = PI / 2 - alpha * PI
                x = a_val * t_val * np.cos(theta)
                y = b_val * np.sin(theta)
                mob.move_to(center + np.array([x, y, 0]))
            return updater

        # まず平坦な空間のボールを移動
        self.play(
            flat_ball1.animate.move_to(flat_final1),
            flat_ball2.animate.move_to(flat_final2),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # 左側の結果表示
        result_flat = Text("平行のまま", font_size=16, color=YELLOW)
        result_flat_en = Text("Still parallel", font_size=12, color=YELLOW_A)
        result_flat_group = VGroup(result_flat, result_flat_en).arrange(DOWN, buff=0.05)
        result_flat_group.next_to(flat_grid, UP, buff=0.1)

        self.play(Write(result_flat_group), run_time=0.4)
        self.wait(0.3)

        # 次に曲がった空間のボールを移動
        self.play(
            UpdateFromAlphaFunc(curved_ball1, create_meridian_updater(right_center, a, b, t1)),
            UpdateFromAlphaFunc(curved_ball2, create_meridian_updater(right_center, a, b, t2)),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # 右側の結果表示
        result_curved = Text("交わった！", font_size=16, color=GREEN)
        result_curved_en = Text("They met!", font_size=12, color=GREEN_A)
        result_curved_group = VGroup(result_curved, result_curved_en).arrange(DOWN, buff=0.05)
        result_curved_group.next_to(curved_grid, UP, buff=0.1)

        # 衝突エフェクト（右側のみ）
        collision_flash = Circle(radius=0.25, color=YELLOW, fill_opacity=0.8)
        collision_flash.move_to(south_pole)

        self.play(
            GrowFromCenter(collision_flash),
            run_time=0.15,
        )
        self.play(
            collision_flash.animate.scale(2).set_opacity(0),
            Write(result_curved_group),
            FadeOut(straight_group),
            run_time=0.4,
        )
        self.remove(collision_flash)

        self.wait(0.5)

        # ===== 結論 =====
        conclusion = Text("曲がった空間では「まっすぐ」が交わる", font_size=22, color=WHITE)
        conclusion_en = Text(
            '"Straight" lines meet in curved space', font_size=14, color=GRAY
        )
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Write(conclusion_group))
        self.wait(2)

    def create_flat_grid(self):
        """平坦な正方形格子を作成"""
        grid = VGroup()
        grid_size = 1.8
        num_lines = 5

        # 縦線
        for i in range(num_lines):
            x = -grid_size + (2 * grid_size / (num_lines - 1)) * i
            line = Line(
                UP * grid_size + RIGHT * x,
                DOWN * grid_size + RIGHT * x,
                color=BLUE_B,
                stroke_width=1.5,
            )
            grid.add(line)

        # 横線
        for i in range(num_lines):
            y = -grid_size + (2 * grid_size / (num_lines - 1)) * i
            line = Line(
                LEFT * grid_size + UP * y,
                RIGHT * grid_size + UP * y,
                color=BLUE_B,
                stroke_width=1.5,
            )
            grid.add(line)

        return grid

    def create_mollweide_grid(self):
        """モルワイデ図法風の格子を作成"""
        grid = VGroup()

        # 楕円のパラメータ
        a = 2.0  # 横幅
        b = 1.7  # 縦幅

        # 外枠（楕円）
        ellipse = Ellipse(width=2 * a, height=2 * b, color=BLUE_B, stroke_width=2)
        grid.add(ellipse)

        # 経線（縦の曲線）- 北極から南極へ
        num_meridians = 7
        for i in range(num_meridians):
            # -1 から 1 までの値
            t = -1 + (2 / (num_meridians - 1)) * i

            # 経線をパラメトリックに描画
            meridian = ParametricFunction(
                lambda theta, t=t: np.array(
                    [
                        a * t * np.cos(theta),  # x: 楕円の形状に合わせる
                        b * np.sin(theta),  # y: 縦方向
                        0,
                    ]
                ),
                t_range=[-PI / 2, PI / 2],
                color=BLUE_B,
                stroke_width=1.5 if i != num_meridians // 2 else 2,
            )
            grid.add(meridian)

        # 緯線（横の曲線）
        num_parallels = 5
        for i in range(num_parallels):
            # -1 から 1 までの値（極を除く）
            v = -0.8 + (1.6 / (num_parallels - 1)) * i

            # 緯線を楕円の一部として描画
            y_pos = b * v
            # この緯度での楕円の幅を計算
            x_width = a * np.sqrt(1 - v**2)

            parallel = Line(
                LEFT * x_width + UP * y_pos,
                RIGHT * x_width + UP * y_pos,
                color=BLUE_B,
                stroke_width=1.5 if abs(v) > 0.01 else 2,  # 赤道は太く
            )
            grid.add(parallel)

        # 北極と南極の点
        north_pole = Dot(UP * b, radius=0.08, color=WHITE)
        south_pole = Dot(DOWN * b, radius=0.08, color=WHITE)
        grid.add(north_pole, south_pole)

        # 極のラベル
        north_label = Text("N", font_size=12, color=WHITE)
        north_label.next_to(north_pole, UP, buff=0.1)
        south_label = Text("S", font_size=12, color=WHITE)
        south_label.next_to(south_pole, DOWN, buff=0.1)
        grid.add(north_label, south_label)

        return grid


class FlatVsCurvedGridSimple(Scene):
    """
    シンプル版：最小構成
    Simple version: Minimal configuration
    """

    def construct(self):
        # 左右の中心
        left_center = LEFT * 3
        right_center = RIGHT * 3

        # 平坦な格子（シンプル）
        flat_grid = VGroup()
        for i in range(5):
            x = -1.5 + 0.75 * i
            flat_grid.add(
                Line(UP * 1.5 + RIGHT * x, DOWN * 1.5 + RIGHT * x, color=BLUE_B, stroke_width=1.5)
            )
        for i in range(5):
            y = -1.5 + 0.75 * i
            flat_grid.add(
                Line(LEFT * 1.5 + UP * y, RIGHT * 1.5 + UP * y, color=BLUE_B, stroke_width=1.5)
            )
        flat_grid.move_to(left_center)

        # モルワイデ風格子（シンプル）
        curved_grid = VGroup()
        a, b = 1.8, 1.5
        ellipse = Ellipse(width=2 * a, height=2 * b, color=BLUE_B, stroke_width=2)
        curved_grid.add(ellipse)

        # 経線
        for t in [-0.6, -0.3, 0, 0.3, 0.6]:
            meridian = ParametricFunction(
                lambda theta, t=t: np.array([a * t * np.cos(theta), b * np.sin(theta), 0]),
                t_range=[-PI / 2, PI / 2],
                color=BLUE_B,
                stroke_width=1.5,
            )
            curved_grid.add(meridian)

        # 極の点
        curved_grid.add(Dot(UP * b, radius=0.06, color=WHITE))
        curved_grid.add(Dot(DOWN * b, radius=0.06, color=WHITE))
        curved_grid.move_to(right_center)

        # ラベル
        flat_label = Text("平坦 / Flat", font_size=14, color=YELLOW)
        flat_label.next_to(flat_grid, DOWN, buff=0.2)
        curved_label = Text("曲がった / Curved", font_size=14, color=GREEN)
        curved_label.next_to(curved_grid, DOWN, buff=0.2)

        self.add(flat_grid, curved_grid, flat_label, curved_label)
        self.wait(0.3)

        # ボール
        ball_radius = 0.08

        # 左側：平坦空間のボール
        flat_ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9).move_to(
            left_center + LEFT * 0.4 + UP * 1.3
        )
        flat_ball2 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9).move_to(
            left_center + RIGHT * 0.4 + UP * 1.3
        )

        # 右側：北極点からスタート
        north_pole = right_center + UP * b
        curved_ball1 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9).move_to(
            north_pole
        )
        curved_ball2 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9).move_to(
            north_pole
        )

        for ball in [flat_ball1, flat_ball2, curved_ball1, curved_ball2]:
            ball.set_stroke(color=WHITE, width=1.5)

        self.play(
            FadeIn(flat_ball1),
            FadeIn(flat_ball2),
            FadeIn(curved_ball1),
            FadeIn(curved_ball2),
            run_time=0.4,
        )

        # 経線に沿った移動（UpdateFromAlphaFuncを使用）
        t1, t2 = -0.3, 0.3

        def create_meridian_updater(center, a_val, b_val, t_val):
            def updater(mob, alpha):
                theta = PI / 2 - alpha * PI
                x = a_val * t_val * np.cos(theta)
                y = b_val * np.sin(theta)
                mob.move_to(center + np.array([x, y, 0]))
            return updater

        # 落下
        self.play(
            flat_ball1.animate.move_to(left_center + LEFT * 0.4 + DOWN * 1.3),
            flat_ball2.animate.move_to(left_center + RIGHT * 0.4 + DOWN * 1.3),
            UpdateFromAlphaFunc(curved_ball1, create_meridian_updater(right_center, a, b, t1)),
            UpdateFromAlphaFunc(curved_ball2, create_meridian_updater(right_center, a, b, t2)),
            run_time=1.8,
            rate_func=rate_functions.ease_in_out_sine,
        )

        south_pole = right_center + DOWN * b

        # 衝突フラッシュ
        flash = Circle(radius=0.2, color=YELLOW, fill_opacity=0.8).move_to(south_pole)
        self.play(GrowFromCenter(flash), run_time=0.1)
        self.play(flash.animate.scale(2).set_opacity(0), run_time=0.2)
        self.remove(flash)

        self.wait(1.5)


class FlatVsCurvedGridWithTrajectory(Scene):
    """
    軌跡付き版：ボールの軌道を線で表示
    Trajectory version: Show ball paths as lines
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("「まっすぐ」なのに交わる？", font_size=28)
        title_en = Text('"Straight" yet they meet?', font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # 左右の中心
        left_center = LEFT * 3.3
        right_center = RIGHT * 3.3

        # ===== 格子作成 =====
        # 平坦な格子
        flat_grid = VGroup()
        grid_size = 1.8
        for i in range(5):
            x = -grid_size + (grid_size / 2) * i
            flat_grid.add(
                Line(
                    UP * grid_size + RIGHT * x,
                    DOWN * grid_size + RIGHT * x,
                    color=BLUE_B,
                    stroke_width=1.5,
                    stroke_opacity=0.6,
                )
            )
        for i in range(5):
            y = -grid_size + (grid_size / 2) * i
            flat_grid.add(
                Line(
                    LEFT * grid_size + UP * y,
                    RIGHT * grid_size + UP * y,
                    color=BLUE_B,
                    stroke_width=1.5,
                    stroke_opacity=0.6,
                )
            )
        flat_grid.move_to(left_center)

        # モルワイデ風格子
        curved_grid = VGroup()
        a, b = 2.0, 1.7
        ellipse = Ellipse(width=2 * a, height=2 * b, color=BLUE_B, stroke_width=2, stroke_opacity=0.6)
        curved_grid.add(ellipse)

        for t in [-0.7, -0.35, 0, 0.35, 0.7]:
            meridian = ParametricFunction(
                lambda theta, t=t: np.array([a * t * np.cos(theta), b * np.sin(theta), 0]),
                t_range=[-PI / 2, PI / 2],
                color=BLUE_B,
                stroke_width=1.5,
                stroke_opacity=0.6,
            )
            curved_grid.add(meridian)

        for v in [-0.6, -0.3, 0, 0.3, 0.6]:
            y_pos = b * v
            x_width = a * np.sqrt(1 - v**2)
            curved_grid.add(
                Line(
                    LEFT * x_width + UP * y_pos,
                    RIGHT * x_width + UP * y_pos,
                    color=BLUE_B,
                    stroke_width=1.5,
                    stroke_opacity=0.6,
                )
            )

        north_pole = Dot(UP * b, radius=0.08, color=WHITE)
        south_pole_dot = Dot(DOWN * b, radius=0.08, color=WHITE)
        curved_grid.add(north_pole, south_pole_dot)
        curved_grid.move_to(right_center)

        # ラベル
        flat_label = Text("平坦 / Flat", font_size=16, color=YELLOW)
        flat_label.next_to(flat_grid, DOWN, buff=0.25)
        curved_label = Text("曲がった / Curved", font_size=16, color=GREEN)
        curved_label.next_to(curved_grid, DOWN, buff=0.25)

        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1)

        self.play(
            Create(flat_grid),
            Create(curved_grid),
            Create(divider),
            run_time=1.0,
        )
        self.play(Write(flat_label), Write(curved_label), run_time=0.4)
        self.wait(0.3)

        # ===== 軌道線（先に表示）=====
        # 左側：平行な直線
        trajectory_flat1 = DashedLine(
            left_center + LEFT * 0.5 + UP * 1.7,
            left_center + LEFT * 0.5 + DOWN * 1.7,
            color=RED_A,
            stroke_width=2,
            dash_length=0.1,
        )
        trajectory_flat2 = DashedLine(
            left_center + RIGHT * 0.5 + UP * 1.7,
            left_center + RIGHT * 0.5 + DOWN * 1.7,
            color=RED_A,
            stroke_width=2,
            dash_length=0.1,
        )

        # 右側：経線に沿った曲線（南極で交わる）
        south_pole = right_center + DOWN * b
        t1, t2 = -0.25, 0.25

        trajectory_curved1 = ParametricFunction(
            lambda theta: right_center
            + np.array([a * t1 * np.cos(theta), b * np.sin(theta), 0]),
            t_range=[-PI / 2, PI / 2],
            color=GREEN_A,
            stroke_width=2,
        )
        trajectory_curved2 = ParametricFunction(
            lambda theta: right_center
            + np.array([a * t2 * np.cos(theta), b * np.sin(theta), 0]),
            t_range=[-PI / 2, PI / 2],
            color=GREEN_A,
            stroke_width=2,
        )

        self.play(
            Create(trajectory_flat1),
            Create(trajectory_flat2),
            Create(trajectory_curved1),
            Create(trajectory_curved2),
            run_time=0.8,
        )

        # ===== ボール =====
        ball_radius = 0.1

        # 左側：平坦空間のボール
        flat_ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        flat_ball1.set_stroke(color=WHITE, width=2)
        flat_ball1.move_to(left_center + LEFT * 0.5 + UP * 1.5)

        flat_ball2 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        flat_ball2.set_stroke(color=WHITE, width=2)
        flat_ball2.move_to(left_center + RIGHT * 0.5 + UP * 1.5)

        # 右側：北極点からスタート
        north_pole = right_center + UP * b
        curved_ball1 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        curved_ball1.set_stroke(color=WHITE, width=2)
        curved_ball1.move_to(north_pole)

        curved_ball2 = Circle(radius=ball_radius, color=GREEN_C, fill_opacity=0.9)
        curved_ball2.set_stroke(color=WHITE, width=2)
        curved_ball2.move_to(north_pole)

        self.play(
            FadeIn(flat_ball1, scale=0.5),
            FadeIn(flat_ball2, scale=0.5),
            FadeIn(curved_ball1, scale=0.5),
            FadeIn(curved_ball2, scale=0.5),
            run_time=0.4,
        )
        self.wait(0.3)

        # ===== 落下アニメーション =====
        fall_duration = 2.2

        # 左側：平行のまま
        flat_final1 = left_center + LEFT * 0.5 + DOWN * 1.5
        flat_final2 = left_center + RIGHT * 0.5 + DOWN * 1.5

        # 経線に沿った移動（UpdateFromAlphaFuncを使用）
        def create_meridian_updater(center, a_val, b_val, t_val):
            def updater(mob, alpha):
                theta = PI / 2 - alpha * PI
                x = a_val * t_val * np.cos(theta)
                y = b_val * np.sin(theta)
                mob.move_to(center + np.array([x, y, 0]))
            return updater

        self.play(
            flat_ball1.animate.move_to(flat_final1),
            flat_ball2.animate.move_to(flat_final2),
            UpdateFromAlphaFunc(curved_ball1, create_meridian_updater(right_center, a, b, t1)),
            UpdateFromAlphaFunc(curved_ball2, create_meridian_updater(right_center, a, b, t2)),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # 衝突エフェクト
        flash = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        flash.move_to(south_pole)
        self.play(GrowFromCenter(flash), run_time=0.15)
        self.play(flash.animate.scale(2).set_opacity(0), run_time=0.25)
        self.remove(flash)

        # ===== 結果 =====
        result_flat = Text("平行のまま", font_size=16, color=YELLOW)
        result_flat.next_to(flat_grid, UP, buff=0.1)

        result_curved = Text("交わった！", font_size=16, color=GREEN)
        result_curved.next_to(curved_grid, UP, buff=0.1)

        self.play(Write(result_flat), Write(result_curved))
        self.wait(0.5)

        # ===== 結論 =====
        conclusion = Text("これが「時空の曲がり」", font_size=24, color=WHITE)
        conclusion_en = Text("This is spacetime curvature", font_size=16, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.3)

        self.play(Write(conclusion_group))
        self.wait(2)


class GravityWellMetric(Scene):
    """
    重力井戸による計量の変化と測地線
    Metric variation due to gravity well and geodesics

    2次元平面上で、中心に重力源があると格子が歪む様子を可視化。
    格子の目盛りでは「まっすぐ」だが、ユークリッド的には曲がって見える。

    yt_script.md L126-128 の解説用（測地線の直感的理解）
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("時空が曲がると「まっすぐ」も変わる", font_size=26)
        title_en = Text("When spacetime curves, 'straight' changes too", font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # ===== パラメータ =====
        grid_size = 2.5  # 格子の半径
        num_lines = 11   # 格子線の数
        well_center = ORIGIN  # 重力井戸の中心
        well_strength = 0.8   # 歪みの強さ
        well_radius = 1.2     # 歪みの影響範囲

        # ===== 変形関数 =====
        def warp_point(point, strength=well_strength, radius=well_radius):
            """
            重力井戸による点の変形
            中心に近いほど格子が密になる（放射方向に縮む）
            """
            x, y = point[0], point[1]
            r = np.sqrt(x**2 + y**2)
            if r < 0.01:
                return point

            # 中心に近いほど放射方向に「引き寄せられる」
            # これにより格子が中心付近で密になる
            factor = 1 - strength * np.exp(-(r / radius) ** 2)
            new_r = r * factor
            return np.array([x * new_r / r, y * new_r / r, 0])

        # ===== 平坦な格子を作成 =====
        flat_grid = VGroup()
        spacing = 2 * grid_size / (num_lines - 1)

        # 縦線
        for i in range(num_lines):
            x = -grid_size + spacing * i
            line = Line(
                np.array([x, -grid_size, 0]),
                np.array([x, grid_size, 0]),
                color=BLUE_B,
                stroke_width=1.5,
                stroke_opacity=0.7,
            )
            flat_grid.add(line)

        # 横線
        for i in range(num_lines):
            y = -grid_size + spacing * i
            line = Line(
                np.array([-grid_size, y, 0]),
                np.array([grid_size, y, 0]),
                color=BLUE_B,
                stroke_width=1.5,
                stroke_opacity=0.7,
            )
            flat_grid.add(line)

        # ===== 歪んだ格子を作成 =====
        warped_grid = VGroup()
        num_segments = 30  # 各線を滑らかにするためのセグメント数

        # 縦線（歪み適用）
        for i in range(num_lines):
            x = -grid_size + spacing * i
            points = []
            for j in range(num_segments + 1):
                y = -grid_size + (2 * grid_size / num_segments) * j
                warped = warp_point(np.array([x, y, 0]))
                points.append(warped)

            warped_line = VMobject(color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7)
            warped_line.set_points_smoothly(points)
            warped_grid.add(warped_line)

        # 横線（歪み適用）
        for i in range(num_lines):
            y = -grid_size + spacing * i
            points = []
            for j in range(num_segments + 1):
                x = -grid_size + (2 * grid_size / num_segments) * j
                warped = warp_point(np.array([x, y, 0]))
                points.append(warped)

            warped_line = VMobject(color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7)
            warped_line.set_points_smoothly(points)
            warped_grid.add(warped_line)

        # ===== 重力源の表示 =====
        gravity_source = Dot(well_center, radius=0.15, color=YELLOW)
        gravity_label = Text("M", font_size=16, color=YELLOW)
        gravity_label.next_to(gravity_source, DOWN, buff=0.15)
        gravity_group = VGroup(gravity_source, gravity_label)

        # ===== まず平坦な格子を表示 =====
        flat_text = Text("平坦な空間", font_size=20, color=WHITE)
        flat_text_en = Text("Flat space", font_size=14, color=GRAY)
        flat_text_group = VGroup(flat_text, flat_text_en).arrange(DOWN, buff=0.05)
        flat_text_group.to_edge(DOWN, buff=0.5)

        self.play(Create(flat_grid), run_time=1.0)
        self.play(Write(flat_text_group), run_time=0.5)
        self.wait(0.5)

        # ===== 重力源を配置して格子を歪める =====
        warp_text = Text("質量があると空間が歪む", font_size=20, color=YELLOW)
        warp_text_en = Text("Mass warps space", font_size=14, color=YELLOW_A)
        warp_text_group = VGroup(warp_text, warp_text_en).arrange(DOWN, buff=0.05)
        warp_text_group.to_edge(DOWN, buff=0.5)

        self.play(
            FadeIn(gravity_group, scale=0.5),
            Transform(flat_text_group, warp_text_group),
            run_time=0.6,
        )
        self.wait(0.3)

        # 格子の変形アニメーション
        self.play(
            Transform(flat_grid, warped_grid),
            run_time=2.0,
            rate_func=rate_functions.ease_in_out_cubic,
        )
        self.wait(0.5)

        # ===== 格子の説明 =====
        metric_text = Text("格子の目盛りが場所によって違う", font_size=18, color=WHITE)
        metric_text_en = Text("Grid spacing varies by location", font_size=12, color=GRAY)
        metric_text_group = VGroup(metric_text, metric_text_en).arrange(DOWN, buff=0.05)
        metric_text_group.to_edge(DOWN, buff=0.5)

        self.play(Transform(flat_text_group, metric_text_group), run_time=0.5)
        self.wait(0.8)

        # ===== 測地線（最短経路）の計算と表示 =====
        # ボールの開始点と終了点（重力井戸を迂回する経路）
        start_point = np.array([-2.0, 1.5, 0])
        end_point = np.array([2.0, -1.0, 0])

        # 測地線の計算（変形空間での最短経路）
        # 簡易的に：重力井戸を避けて曲がる経路を数値的に生成
        def compute_geodesic(start, end, num_points=50):
            """
            変形空間での測地線を近似計算
            中心付近は「距離が長い」ので迂回する経路が最短になる
            """
            # 直線経路
            direct_path = [
                start + (end - start) * t / (num_points - 1)
                for t in range(num_points)
            ]

            # 重力井戸の影響で曲がる経路を計算
            # 簡易モデル：中心からの距離に応じて経路を外側に押し出す
            geodesic_points = []
            for i, p in enumerate(direct_path):
                t = i / (num_points - 1)
                # 経路の中央付近で最大の迂回
                deflection = np.sin(t * PI) ** 2

                # 中心からの方向
                r = np.sqrt(p[0]**2 + p[1]**2)
                if r > 0.1:
                    # 中心から離れる方向に押し出す
                    push_strength = 0.6 * deflection * np.exp(-(r / 1.5)**2)
                    push_dir = np.array([p[0] / r, p[1] / r, 0])
                    new_p = p + push_dir * push_strength
                else:
                    new_p = p
                geodesic_points.append(new_p)

            return geodesic_points

        geodesic_points = compute_geodesic(start_point, end_point)

        # 測地線の描画
        geodesic_line = VMobject(color=ORANGE, stroke_width=4)
        geodesic_line.set_points_smoothly(geodesic_points)

        # 直線（ユークリッド的最短）も表示して比較
        euclidean_line = DashedLine(
            start_point, end_point,
            color=RED_A,
            stroke_width=2,
            dash_length=0.15,
        )

        # ボール
        ball = Circle(radius=0.12, color=ORANGE, fill_opacity=0.9)
        ball.set_stroke(color=WHITE, width=2)
        ball.move_to(start_point)

        # 開始点と終了点のマーカー
        start_marker = Dot(start_point, radius=0.08, color=GREEN_C)
        end_marker = Dot(end_point, radius=0.08, color=GREEN_C)
        start_label = Text("A", font_size=14, color=GREEN_C)
        start_label.next_to(start_marker, UP + LEFT, buff=0.1)
        end_label = Text("B", font_size=14, color=GREEN_C)
        end_label.next_to(end_marker, DOWN + RIGHT, buff=0.1)

        self.play(
            FadeIn(start_marker),
            FadeIn(end_marker),
            Write(start_label),
            Write(end_label),
            run_time=0.5,
        )

        # 直線を表示（これは最短ではない！）
        euclidean_text = Text("ユークリッド的な直線", font_size=16, color=RED_A)
        euclidean_text_en = Text("Euclidean straight line", font_size=12, color=RED_A)
        euclidean_text_group = VGroup(euclidean_text, euclidean_text_en).arrange(DOWN, buff=0.05)
        euclidean_text_group.to_edge(DOWN, buff=0.5)

        self.play(
            Create(euclidean_line),
            Transform(flat_text_group, euclidean_text_group),
            run_time=0.8,
        )
        self.wait(0.5)

        # ===== 測地線を表示 =====
        geodesic_text = Text("格子の目盛りで測った最短経路（測地線）", font_size=16, color=ORANGE)
        geodesic_text_en = Text("Shortest path in grid metric (Geodesic)", font_size=12, color=ORANGE)
        geodesic_text_group = VGroup(geodesic_text, geodesic_text_en).arrange(DOWN, buff=0.05)
        geodesic_text_group.to_edge(DOWN, buff=0.5)

        self.play(
            Create(geodesic_line),
            Transform(flat_text_group, geodesic_text_group),
            run_time=1.2,
        )
        self.wait(0.3)

        # ===== ボールが測地線に沿って移動 =====
        self.play(FadeIn(ball, scale=0.5), run_time=0.3)

        self.play(
            MoveAlongPath(ball, geodesic_line),
            run_time=2.5,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(0.5)

        # ===== 結論 =====
        conclusion = Text("曲がって見えるけど、これが「まっすぐ」", font_size=22, color=WHITE)
        conclusion_en = Text('Looks curved, but this IS "straight"', font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(flat_text_group, conclusion_group), run_time=0.6)
        self.wait(1.0)


class GravityWellMetricComparison(Scene):
    """
    左右比較版：平坦 vs 重力井戸
    Side-by-side comparison: Flat vs Gravity well
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("平坦な空間 vs 歪んだ空間", font_size=26)
        title_en = Text("Flat Space vs Warped Space", font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # ===== パラメータ =====
        grid_size = 1.6
        num_lines = 9
        well_strength = 0.7
        well_radius = 0.9

        left_center = LEFT * 3.3
        right_center = RIGHT * 3.3

        # ===== 変形関数 =====
        def warp_point(point, center, strength=well_strength, radius=well_radius):
            rel = point - center
            x, y = rel[0], rel[1]
            r = np.sqrt(x**2 + y**2)
            if r < 0.01:
                return point
            factor = 1 - strength * np.exp(-(r / radius) ** 2)
            new_r = r * factor
            return center + np.array([x * new_r / r, y * new_r / r, 0])

        # ===== 左側：平坦な格子 =====
        flat_grid = VGroup()
        spacing = 2 * grid_size / (num_lines - 1)

        for i in range(num_lines):
            x = -grid_size + spacing * i
            flat_grid.add(Line(
                left_center + np.array([x, -grid_size, 0]),
                left_center + np.array([x, grid_size, 0]),
                color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7,
            ))
        for i in range(num_lines):
            y = -grid_size + spacing * i
            flat_grid.add(Line(
                left_center + np.array([-grid_size, y, 0]),
                left_center + np.array([grid_size, y, 0]),
                color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7,
            ))

        flat_label = Text("平坦 / Flat", font_size=16, color=YELLOW)
        flat_label.next_to(flat_grid, DOWN, buff=0.25)

        # ===== 右側：歪んだ格子 =====
        warped_grid = VGroup()
        num_segments = 25

        for i in range(num_lines):
            x = -grid_size + spacing * i
            points = []
            for j in range(num_segments + 1):
                y = -grid_size + (2 * grid_size / num_segments) * j
                p = right_center + np.array([x, y, 0])
                warped = warp_point(p, right_center)
                points.append(warped)
            warped_line = VMobject(color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7)
            warped_line.set_points_smoothly(points)
            warped_grid.add(warped_line)

        for i in range(num_lines):
            y = -grid_size + spacing * i
            points = []
            for j in range(num_segments + 1):
                x = -grid_size + (2 * grid_size / num_segments) * j
                p = right_center + np.array([x, y, 0])
                warped = warp_point(p, right_center)
                points.append(warped)
            warped_line = VMobject(color=BLUE_B, stroke_width=1.5, stroke_opacity=0.7)
            warped_line.set_points_smoothly(points)
            warped_grid.add(warped_line)

        # 重力源
        gravity_source = Dot(right_center, radius=0.12, color=YELLOW)
        gravity_label_m = Text("M", font_size=14, color=YELLOW)
        gravity_label_m.next_to(gravity_source, DOWN, buff=0.1)

        warped_label = Text("歪んだ / Warped", font_size=16, color=GREEN)
        warped_label.next_to(warped_grid, DOWN, buff=0.25)

        # 区切り線
        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1)

        # 格子を表示
        self.play(
            Create(flat_grid),
            Create(warped_grid),
            Create(divider),
            FadeIn(gravity_source),
            Write(gravity_label_m),
            run_time=1.2,
        )
        self.play(Write(flat_label), Write(warped_label), run_time=0.4)
        self.wait(0.5)

        # ===== ボールと経路 =====
        # 左側：直線経路
        left_start = left_center + np.array([-1.3, 1.0, 0])
        left_end = left_center + np.array([1.3, -0.8, 0])

        flat_path = Line(left_start, left_end, color=ORANGE, stroke_width=3)

        flat_ball = Circle(radius=0.1, color=ORANGE, fill_opacity=0.9)
        flat_ball.set_stroke(color=WHITE, width=2)
        flat_ball.move_to(left_start)

        # 右側：測地線（迂回経路）
        right_start = right_center + np.array([-1.3, 1.0, 0])
        right_end = right_center + np.array([1.3, -0.8, 0])

        def compute_geodesic_right(start, end, center, num_points=40):
            geodesic_points = []
            for i in range(num_points):
                t = i / (num_points - 1)
                p = start + (end - start) * t
                deflection = np.sin(t * PI) ** 2
                rel = p - center
                r = np.sqrt(rel[0]**2 + rel[1]**2)
                if r > 0.1:
                    push_strength = 0.5 * deflection * np.exp(-(r / 1.0)**2)
                    push_dir = rel / r
                    new_p = p + push_dir * push_strength
                else:
                    new_p = p
                geodesic_points.append(new_p)
            return geodesic_points

        geodesic_points = compute_geodesic_right(right_start, right_end, right_center)
        warped_path = VMobject(color=ORANGE, stroke_width=3)
        warped_path.set_points_smoothly(geodesic_points)

        warped_ball = Circle(radius=0.1, color=ORANGE, fill_opacity=0.9)
        warped_ball.set_stroke(color=WHITE, width=2)
        warped_ball.move_to(right_start)

        # 開始・終了マーカー
        markers = VGroup(
            Dot(left_start, radius=0.06, color=GREEN_C),
            Dot(left_end, radius=0.06, color=GREEN_C),
            Dot(right_start, radius=0.06, color=GREEN_C),
            Dot(right_end, radius=0.06, color=GREEN_C),
        )

        self.play(FadeIn(markers), run_time=0.3)

        # 経路を表示
        path_text = Text("どちらも「最短経路」", font_size=20, color=ORANGE)
        path_text_en = Text("Both are 'shortest paths'", font_size=14, color=ORANGE)
        path_text_group = VGroup(path_text, path_text_en).arrange(DOWN, buff=0.05)
        path_text_group.to_edge(DOWN, buff=0.4)

        self.play(
            Create(flat_path),
            Create(warped_path),
            Write(path_text_group),
            run_time=1.0,
        )
        self.wait(0.3)

        # ボールを移動
        self.play(
            FadeIn(flat_ball, scale=0.5),
            FadeIn(warped_ball, scale=0.5),
            run_time=0.3,
        )

        self.play(
            MoveAlongPath(flat_ball, flat_path),
            MoveAlongPath(warped_ball, warped_path),
            run_time=2.5,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(0.5)

        # 結論
        conclusion = Text("計量が違えば「まっすぐ」も違う", font_size=22, color=WHITE)
        conclusion_en = Text("Different metrics mean different 'straight'", font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(path_text_group, conclusion_group), run_time=0.6)
        self.wait(2)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/flat_vs_curved_grid.py FlatVsCurvedGrid")
    print("  manim -pql scripts/flat_vs_curved_grid.py FlatVsCurvedGridSimple")
    print("  manim -pql scripts/flat_vs_curved_grid.py FlatVsCurvedGridWithTrajectory")
    print("  manim -pql scripts/flat_vs_curved_grid.py GravityWellMetric")
    print("  manim -pql scripts/flat_vs_curved_grid.py GravityWellMetricComparison")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  FlatVsCurvedGrid           - 基本版（格子の対比）")
    print("                               Basic version (grid comparison)")
    print("  FlatVsCurvedGridSimple     - シンプル版（最小構成）")
    print("                               Simple version (minimal)")
    print("  FlatVsCurvedGridWithTrajectory - 軌跡付き版（ボールの軌道を表示）")
    print("                                   Trajectory version (show ball paths)")
    print("  GravityWellMetric          - 重力井戸版（計量変化と測地線）")
    print("                               Gravity well version (metric change & geodesic)")
    print("  GravityWellMetricComparison - 重力井戸比較版（平坦 vs 歪んだ空間）")
    print("                                Gravity well comparison (flat vs warped)")
