"""
時空図における測地線の収束アニメーション
Spacetime Diagram: Geodesic Convergence Animation

時空図上で「まっすぐ」な2本の世界線（測地線）が収束していく様子を可視化。
「力が働いていないのに間隔が変わる」というパラドックスを時空の言葉で説明する。

Visualizes two "straight" worldlines (geodesics) converging in a spacetime diagram.
Explains the paradox of "changing separation without force" in spacetime language.

yt_script.md L112-118 の解説用
L126「測地線」、L130「測地線偏差」への伏線
"""

from manim import *
import numpy as np


class SpacetimeGeodesicConvergence(Scene):
    """
    時空図で2本の測地線が収束する様子を表示
    Shows two geodesics converging in a spacetime diagram
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("時空図で見る「まっすぐ」", font_size=28)
        title_en = Text('"Straight" in Spacetime Diagram', font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.5)

        # ===== 座標軸 =====
        # 時空図の軸を作成
        origin = DOWN * 1.5 + LEFT * 0.5

        # 時間軸（縦）
        time_axis = Arrow(
            origin + DOWN * 0.3,
            origin + UP * 4.5,
            color=WHITE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )
        time_label = Text("時間", font_size=16, color=WHITE)
        time_label_en = Text("Time", font_size=12, color=GRAY)
        time_label_group = VGroup(time_label, time_label_en).arrange(DOWN, buff=0.05)
        time_label_group.next_to(time_axis.get_end(), RIGHT, buff=0.1)

        # 空間軸（横）
        space_axis = Arrow(
            origin + LEFT * 0.3,
            origin + RIGHT * 5.5,
            color=WHITE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )
        space_label = Text("空間", font_size=16, color=WHITE)
        space_label_en = Text("Space", font_size=12, color=GRAY)
        space_label_group = VGroup(space_label, space_label_en).arrange(DOWN, buff=0.05)
        space_label_group.next_to(space_axis.get_end(), DOWN, buff=0.1)

        self.play(
            GrowArrow(time_axis),
            GrowArrow(space_axis),
            run_time=0.8,
        )
        self.play(
            Write(time_label_group),
            Write(space_label_group),
            run_time=0.5,
        )
        self.wait(0.3)

        # ===== 世界線（測地線）の定義 =====
        # 2本の世界線：最初は離れているが、時間とともに近づく
        # 曲がった時空では「直線」が収束する

        # 世界線のパラメータ
        start_separation = 2.5  # 初期の空間的距離
        end_separation = 0.3    # 最終的な空間的距離
        world_line_height = 3.5  # 時間方向の長さ

        # 世界線1（左側）の経路
        def worldline1_path(t):
            # t: 0 -> 1 (正規化された時間パラメータ)
            x = origin[0] + 1.0 + (start_separation / 2) * (1 - t) + (end_separation / 2) * t
            y = origin[1] + t * world_line_height
            return np.array([x, y, 0])

        # 世界線2（右側）の経路
        def worldline2_path(t):
            x = origin[0] + 1.0 + start_separation - (start_separation / 2) * (1 - t) - (end_separation / 2) * t
            y = origin[1] + t * world_line_height
            return np.array([x, y, 0])

        # 世界線を曲線として作成
        worldline1 = ParametricFunction(
            worldline1_path,
            t_range=[0, 1],
            color=RED_C,
            stroke_width=4,
        )
        worldline2 = ParametricFunction(
            worldline2_path,
            t_range=[0, 1],
            color=BLUE_C,
            stroke_width=4,
        )

        # ===== 「まっすぐ」であることを示すラベル =====
        straight_label1 = Text("まっすぐ", font_size=14, color=RED_A)
        straight_label1_en = Text("Straight", font_size=10, color=RED_A)
        straight_group1 = VGroup(straight_label1, straight_label1_en).arrange(DOWN, buff=0.02)
        straight_group1.next_to(worldline1.point_from_proportion(0.3), LEFT, buff=0.15)

        straight_label2 = Text("まっすぐ", font_size=14, color=BLUE_A)
        straight_label2_en = Text("Straight", font_size=10, color=BLUE_A)
        straight_group2 = VGroup(straight_label2, straight_label2_en).arrange(DOWN, buff=0.02)
        straight_group2.next_to(worldline2.point_from_proportion(0.3), RIGHT, buff=0.15)

        # ===== ボール（物体）を配置 =====
        ball_radius = 0.15
        ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball1.set_stroke(color=WHITE, width=2)
        ball1.move_to(worldline1_path(0))

        ball2 = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball2.set_stroke(color=WHITE, width=2)
        ball2.move_to(worldline2_path(0))

        # 初期状態の説明
        initial_text = Text("2つの物体が離れた位置からスタート", font_size=18)
        initial_text_en = Text("Two objects start at separate positions", font_size=14, color=GRAY)
        initial_group = VGroup(initial_text, initial_text_en).arrange(DOWN, buff=0.05)
        initial_group.to_edge(DOWN, buff=0.4)

        self.play(
            FadeIn(ball1, scale=0.5),
            FadeIn(ball2, scale=0.5),
            Write(initial_group),
            run_time=0.6,
        )
        self.wait(0.5)

        # ===== 世界線を描きながらボールが移動 =====
        # 「まっすぐ進んでいる」ことを強調
        moving_text = Text("どちらも「まっすぐ」進んでいる", font_size=18, color=YELLOW)
        moving_text_en = Text('Both are moving "straight"', font_size=14, color=YELLOW_A)
        moving_group = VGroup(moving_text, moving_text_en).arrange(DOWN, buff=0.05)
        moving_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(initial_group, moving_group))

        # 世界線を描画しながらボールを移動
        self.play(
            Create(worldline1),
            Create(worldline2),
            MoveAlongPath(ball1, worldline1),
            MoveAlongPath(ball2, worldline2),
            run_time=3.0,
            rate_func=rate_functions.linear,
        )

        # 「まっすぐ」ラベルを表示
        self.play(
            Write(straight_group1),
            Write(straight_group2),
            run_time=0.5,
        )
        self.wait(0.5)

        # ===== 間隔の変化を示す =====
        # 初期間隔と最終間隔を示す矢印

        # 初期間隔（下部）
        initial_sep_line = DoubleArrow(
            worldline1_path(0) + DOWN * 0.3,
            worldline2_path(0) + DOWN * 0.3,
            color=GREEN_C,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.1,
            buff=0,
        )
        initial_sep_label = Text("広い", font_size=14, color=GREEN_C)
        initial_sep_label.next_to(initial_sep_line, DOWN, buff=0.1)

        # 最終間隔（上部）
        final_sep_line = DoubleArrow(
            worldline1_path(1) + UP * 0.3,
            worldline2_path(1) + UP * 0.3,
            color=ORANGE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
            buff=0,
        )
        final_sep_label = Text("狭い！", font_size=14, color=ORANGE)
        final_sep_label.next_to(final_sep_line, UP, buff=0.1)

        self.play(
            GrowArrow(initial_sep_line),
            Write(initial_sep_label),
            GrowArrow(final_sep_line),
            Write(final_sep_label),
            run_time=0.8,
        )
        self.wait(0.5)

        # ===== パラドックスの提示 =====
        paradox_text = Text("「まっすぐ」なのに間隔が縮む？", font_size=22, color=YELLOW)
        paradox_text_en = Text('"Straight" yet the gap shrinks?', font_size=16, color=YELLOW_A)
        paradox_group = VGroup(paradox_text, paradox_text_en).arrange(DOWN, buff=0.08)
        paradox_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(initial_group, paradox_group))
        self.wait(1.0)

        # ===== 結論への伏線 =====
        conclusion_text = Text("これが「時空の曲がり」の証拠", font_size=22, color=WHITE)
        conclusion_text_en = Text("This is evidence of curved spacetime", font_size=16, color=GRAY)
        conclusion_group = VGroup(conclusion_text, conclusion_text_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(initial_group, conclusion_group))
        self.wait(2)


class SpacetimeGeodesicSimple(Scene):
    """
    シンプル版：最小構成の時空図
    Simple version: Minimal spacetime diagram
    """

    def construct(self):
        # 座標軸（シンプル）
        origin = DOWN * 1.5

        time_axis = Arrow(origin, origin + UP * 4, color=WHITE, stroke_width=2)
        space_axis = Arrow(origin + LEFT * 3, origin + RIGHT * 3, color=WHITE, stroke_width=2)

        time_label = Text("時間 / Time", font_size=14, color=GRAY)
        time_label.next_to(time_axis.get_end(), RIGHT, buff=0.1)
        space_label = Text("空間 / Space", font_size=14, color=GRAY)
        space_label.next_to(space_axis.get_end(), DOWN, buff=0.1)

        self.add(time_axis, space_axis, time_label, space_label)

        # 世界線（収束する2本の線）
        start_sep = 2.0
        end_sep = 0.2
        height = 3.5

        line1 = Line(
            origin + LEFT * (start_sep / 2),
            origin + UP * height + LEFT * (end_sep / 2),
            color=RED_C,
            stroke_width=4,
        )
        line2 = Line(
            origin + RIGHT * (start_sep / 2),
            origin + UP * height + RIGHT * (end_sep / 2),
            color=BLUE_C,
            stroke_width=4,
        )

        # ボール
        ball1 = Circle(radius=0.12, color=RED_C, fill_opacity=0.9)
        ball1.set_stroke(color=WHITE, width=2)
        ball1.move_to(line1.get_start())

        ball2 = Circle(radius=0.12, color=BLUE_C, fill_opacity=0.9)
        ball2.set_stroke(color=WHITE, width=2)
        ball2.move_to(line2.get_start())

        self.play(FadeIn(ball1), FadeIn(ball2), run_time=0.3)

        # 世界線を描きながら移動
        self.play(
            Create(line1),
            Create(line2),
            ball1.animate.move_to(line1.get_end()),
            ball2.animate.move_to(line2.get_end()),
            run_time=2.0,
            rate_func=rate_functions.linear,
        )

        # ラベル
        label1 = Text("まっすぐ", font_size=12, color=RED_A)
        label1.next_to(line1.get_center(), LEFT, buff=0.1)
        label2 = Text("まっすぐ", font_size=12, color=BLUE_A)
        label2.next_to(line2.get_center(), RIGHT, buff=0.1)

        self.play(Write(label1), Write(label2), run_time=0.4)

        # 結論
        conclusion = Text("「まっすぐ」なのに交わる", font_size=20, color=YELLOW)
        conclusion.to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait(1.5)


class SpacetimeGeodesicWithGeodesicLabel(Scene):
    """
    測地線ラベル付き版：L126への橋渡し
    Version with geodesic label: Bridge to L126
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("時空図と測地線", font_size=28)
        title_en = Text("Spacetime Diagram & Geodesics", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # ===== 座標軸 =====
        origin = DOWN * 1.2 + LEFT * 0.5

        time_axis = Arrow(
            origin + DOWN * 0.2,
            origin + UP * 4.0,
            color=WHITE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )
        space_axis = Arrow(
            origin + LEFT * 0.2,
            origin + RIGHT * 5.0,
            color=WHITE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )

        time_label = Text("時間 / Time", font_size=14, color=GRAY)
        time_label.next_to(time_axis.get_end(), RIGHT, buff=0.1)
        space_label = Text("空間 / Space", font_size=14, color=GRAY)
        space_label.next_to(space_axis.get_end(), DOWN, buff=0.1)

        self.play(
            GrowArrow(time_axis),
            GrowArrow(space_axis),
            Write(time_label),
            Write(space_label),
            run_time=0.6,
        )

        # ===== 測地線の定義 =====
        start_sep = 2.2
        end_sep = 0.25
        height = 3.2

        def geodesic1_path(t):
            x = origin[0] + 1.2 + (start_sep / 2) * (1 - t) + (end_sep / 2) * t
            y = origin[1] + t * height
            return np.array([x, y, 0])

        def geodesic2_path(t):
            x = origin[0] + 1.2 + start_sep - (start_sep / 2) * (1 - t) - (end_sep / 2) * t
            y = origin[1] + t * height
            return np.array([x, y, 0])

        geodesic1 = ParametricFunction(
            geodesic1_path,
            t_range=[0, 1],
            color=RED_C,
            stroke_width=4,
        )
        geodesic2 = ParametricFunction(
            geodesic2_path,
            t_range=[0, 1],
            color=BLUE_C,
            stroke_width=4,
        )

        # ボール
        ball_radius = 0.13
        ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        ball1.set_stroke(color=WHITE, width=2)
        ball1.move_to(geodesic1_path(0))

        ball2 = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        ball2.set_stroke(color=WHITE, width=2)
        ball2.move_to(geodesic2_path(0))

        self.play(FadeIn(ball1, scale=0.5), FadeIn(ball2, scale=0.5), run_time=0.4)

        # 説明テキスト
        explain1 = Text("自由落下する物体の軌道を", font_size=18)
        explain1_en = Text("The path of a free-falling object", font_size=14, color=GRAY)
        explain_group1 = VGroup(explain1, explain1_en).arrange(DOWN, buff=0.05)
        explain_group1.to_edge(DOWN, buff=0.4)

        self.play(Write(explain_group1))
        self.wait(0.5)

        # 世界線を描画
        self.play(
            Create(geodesic1),
            Create(geodesic2),
            MoveAlongPath(ball1, geodesic1),
            MoveAlongPath(ball2, geodesic2),
            run_time=2.5,
            rate_func=rate_functions.linear,
        )

        # 「測地線」という言葉を導入
        explain2 = Text("「測地線」と呼びます", font_size=18, color=YELLOW)
        explain2_en = Text('is called a "Geodesic"', font_size=14, color=YELLOW_A)
        explain_group2 = VGroup(explain2, explain2_en).arrange(DOWN, buff=0.05)
        explain_group2.to_edge(DOWN, buff=0.4)

        self.play(Transform(explain_group1, explain_group2))

        # 測地線ラベル
        geodesic_label1 = Text("測地線", font_size=14, color=RED_A)
        geodesic_label1_en = Text("Geodesic", font_size=10, color=RED_A)
        geodesic_group1 = VGroup(geodesic_label1, geodesic_label1_en).arrange(DOWN, buff=0.02)
        geodesic_group1.next_to(geodesic1.point_from_proportion(0.5), LEFT, buff=0.15)

        geodesic_label2 = Text("測地線", font_size=14, color=BLUE_A)
        geodesic_label2_en = Text("Geodesic", font_size=10, color=BLUE_A)
        geodesic_group2 = VGroup(geodesic_label2, geodesic_label2_en).arrange(DOWN, buff=0.02)
        geodesic_group2.next_to(geodesic2.point_from_proportion(0.5), RIGHT, buff=0.15)

        self.play(Write(geodesic_group1), Write(geodesic_group2), run_time=0.6)
        self.wait(0.5)

        # 収束を示す矢印
        convergence_arrow = Arrow(
            geodesic1_path(0.8) + LEFT * 0.2,
            geodesic2_path(0.8) + RIGHT * 0.2,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )
        # 中央に配置
        convergence_arrow.move_to((geodesic1_path(0.85) + geodesic2_path(0.85)) / 2)
        convergence_arrow.scale(0.6)

        convergence_label = Text("収束", font_size=14, color=ORANGE)
        convergence_label_en = Text("Converging", font_size=10, color=ORANGE)
        convergence_group = VGroup(convergence_label, convergence_label_en).arrange(DOWN, buff=0.02)
        convergence_group.next_to(convergence_arrow, UP, buff=0.1)

        self.play(
            GrowArrow(convergence_arrow),
            Write(convergence_group),
            run_time=0.5,
        )
        self.wait(0.5)

        # 結論
        conclusion = Text("2本の測地線の間隔が変化する", font_size=20, color=WHITE)
        conclusion_en = Text("The separation between geodesics changes", font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(explain_group1, conclusion_group))
        self.wait(0.5)

        # 測地線偏差への伏線
        final = Text("→ これを「測地線偏差」と呼ぶ", font_size=20, color=YELLOW)
        final_en = Text('→ This is called "Geodesic Deviation"', font_size=14, color=YELLOW_A)
        final_group = VGroup(final, final_en).arrange(DOWN, buff=0.08)
        final_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(explain_group1, final_group))
        self.wait(2)


class SpacetimeGeodesicComparison(Scene):
    """
    比較版：平坦な時空 vs 曲がった時空
    Comparison version: Flat spacetime vs Curved spacetime
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("平坦な時空 vs 曲がった時空", font_size=26)
        title_en = Text("Flat Spacetime vs Curved Spacetime", font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group))
        self.wait(0.3)

        # ===== 左側：平坦な時空 =====
        left_center = LEFT * 3.3 + DOWN * 0.3

        # 座標軸（左）
        left_origin = left_center + DOWN * 1.5 + LEFT * 1.0
        left_time = Arrow(
            left_origin,
            left_origin + UP * 3.2,
            color=WHITE,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08,
        )
        left_space = Arrow(
            left_origin,
            left_origin + RIGHT * 2.5,
            color=WHITE,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08,
        )

        # 平行な世界線（平坦な時空）
        flat_line1 = Line(
            left_origin + RIGHT * 0.5,
            left_origin + RIGHT * 0.5 + UP * 2.8,
            color=RED_C,
            stroke_width=3,
        )
        flat_line2 = Line(
            left_origin + RIGHT * 1.8,
            left_origin + RIGHT * 1.8 + UP * 2.8,
            color=BLUE_C,
            stroke_width=3,
        )

        flat_label = Text("平坦 / Flat", font_size=16, color=YELLOW)
        flat_label.next_to(left_center + UP * 1.2, UP, buff=0.1)

        # ===== 右側：曲がった時空 =====
        right_center = RIGHT * 3.3 + DOWN * 0.3

        # 座標軸（右）
        right_origin = right_center + DOWN * 1.5 + LEFT * 1.0
        right_time = Arrow(
            right_origin,
            right_origin + UP * 3.2,
            color=WHITE,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08,
        )
        right_space = Arrow(
            right_origin,
            right_origin + RIGHT * 2.5,
            color=WHITE,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08,
        )

        # 収束する世界線（曲がった時空）
        curved_line1 = Line(
            right_origin + RIGHT * 0.5,
            right_origin + RIGHT * 1.0 + UP * 2.8,
            color=RED_C,
            stroke_width=3,
        )
        curved_line2 = Line(
            right_origin + RIGHT * 1.8,
            right_origin + RIGHT * 1.3 + UP * 2.8,
            color=BLUE_C,
            stroke_width=3,
        )

        curved_label = Text("曲がった / Curved", font_size=16, color=GREEN)
        curved_label.next_to(right_center + UP * 1.2, UP, buff=0.1)

        # 区切り線
        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=GRAY, stroke_width=1)

        # 表示
        self.play(
            GrowArrow(left_time),
            GrowArrow(left_space),
            GrowArrow(right_time),
            GrowArrow(right_space),
            Create(divider),
            run_time=0.6,
        )

        self.play(
            Write(flat_label),
            Write(curved_label),
            run_time=0.4,
        )

        # ボール
        ball_radius = 0.1

        flat_ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        flat_ball1.set_stroke(color=WHITE, width=2)
        flat_ball1.move_to(flat_line1.get_start())

        flat_ball2 = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        flat_ball2.set_stroke(color=WHITE, width=2)
        flat_ball2.move_to(flat_line2.get_start())

        curved_ball1 = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.9)
        curved_ball1.set_stroke(color=WHITE, width=2)
        curved_ball1.move_to(curved_line1.get_start())

        curved_ball2 = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.9)
        curved_ball2.set_stroke(color=WHITE, width=2)
        curved_ball2.move_to(curved_line2.get_start())

        self.play(
            FadeIn(flat_ball1, scale=0.5),
            FadeIn(flat_ball2, scale=0.5),
            FadeIn(curved_ball1, scale=0.5),
            FadeIn(curved_ball2, scale=0.5),
            run_time=0.4,
        )

        # 世界線を描画
        self.play(
            Create(flat_line1),
            Create(flat_line2),
            Create(curved_line1),
            Create(curved_line2),
            flat_ball1.animate.move_to(flat_line1.get_end()),
            flat_ball2.animate.move_to(flat_line2.get_end()),
            curved_ball1.animate.move_to(curved_line1.get_end()),
            curved_ball2.animate.move_to(curved_line2.get_end()),
            run_time=2.0,
            rate_func=rate_functions.linear,
        )

        # 結果ラベル
        result_flat = Text("平行のまま", font_size=14, color=YELLOW)
        result_flat_en = Text("Stay parallel", font_size=10, color=YELLOW_A)
        result_flat_group = VGroup(result_flat, result_flat_en).arrange(DOWN, buff=0.02)
        result_flat_group.next_to(flat_line1.get_end(), RIGHT, buff=0.3)

        result_curved = Text("収束！", font_size=14, color=GREEN)
        result_curved_en = Text("Converge!", font_size=10, color=GREEN_A)
        result_curved_group = VGroup(result_curved, result_curved_en).arrange(DOWN, buff=0.02)
        result_curved_group.next_to(
            (curved_line1.get_end() + curved_line2.get_end()) / 2,
            UP,
            buff=0.15,
        )

        self.play(
            Write(result_flat_group),
            Write(result_curved_group),
            run_time=0.5,
        )
        self.wait(0.5)

        # 結論
        conclusion = Text("時空の曲がりが測地線を収束させる", font_size=20, color=WHITE)
        conclusion_en = Text("Spacetime curvature makes geodesics converge", font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Write(conclusion_group))
        self.wait(2)


class GeodesicShortestPath3D(ThreeDScene):
    """
    3D球面上の測地線（大圏コース）アニメーション
    Geodesic (great circle) on a 3D sphere

    yt_script.md L126-128 の解説用
    「曲がって見えるけど実は最短経路」を視覚化
    """

    def construct(self):
        # ===== カメラ設定 =====
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # ===== タイトル（固定テキスト）=====
        title = Text("測地線 = 最短経路", font_size=32)
        title_en = Text("Geodesic = Shortest Path", font_size=20, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_corner(UL, buff=0.3)
        self.add_fixed_in_frame_mobjects(title_group)

        self.play(Write(title_group), run_time=0.8)
        self.wait(0.3)

        # ===== 球面（不透明な3D球）=====
        sphere_radius = 2.0

        sphere = Surface(
            lambda u, v: np.array([
                sphere_radius * np.cos(u) * np.cos(v),
                sphere_radius * np.sin(u) * np.cos(v),
                sphere_radius * np.sin(v),
            ]),
            u_range=[0, TAU],
            v_range=[-PI / 2, PI / 2],
            resolution=(32, 16),
            fill_opacity=1.0,
            stroke_width=0.5,
            stroke_color=BLUE_B,
            fill_color=BLUE_E,
            checkerboard_colors=[BLUE_E, BLUE_D],
        )

        self.add(sphere)
        self.wait(0.3)

        # ===== 2つの点を配置（異なる緯度で測地線の曲がりを強調）=====
        # カメラ: phi=70°, theta=-45° なので、前面は経度-45°付近
        # 点A: 北半球（緯度40°、経度-70°）
        # 点B: 南半球（緯度-30°、経度10°）
        lat_A, lon_A = 40 * DEGREES, -70 * DEGREES
        lat_B, lon_B = -30 * DEGREES, 10 * DEGREES

        def spherical_to_cartesian(lat, lon, r=sphere_radius):
            return np.array([
                r * np.cos(lat) * np.cos(lon),
                r * np.cos(lat) * np.sin(lon),
                r * np.sin(lat),
            ])

        point_A = spherical_to_cartesian(lat_A, lon_A)
        point_B = spherical_to_cartesian(lat_B, lon_B)

        dot_A = Sphere(radius=0.12, color=RED_C).move_to(point_A)
        dot_B = Sphere(radius=0.12, color=GREEN_C).move_to(point_B)

        # ラベルをフレームに固定して左下に配置
        label_info = Text("A → B への経路を比較", font_size=16, color=WHITE)
        label_info_en = Text("Comparing paths from A to B", font_size=12, color=GRAY)
        label_group = VGroup(label_info, label_info_en).arrange(DOWN, buff=0.05)
        label_group.to_corner(DL, buff=0.3)
        self.add_fixed_in_frame_mobjects(label_group)

        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(dot_B, scale=0.5),
            Write(label_group),
            run_time=0.6,
        )
        self.wait(0.3)

        # ===== 緯度線に沿った経路（非最短）=====
        latitude_path = ParametricFunction(
            lambda t: spherical_to_cartesian(lat_A, lon_A + t * (lon_B - lon_A)),
            t_range=[0, 1],
            color=YELLOW,
            stroke_width=4,
        )

        not_shortest_label = Text("緯度線に沿った経路", font_size=18, color=YELLOW)
        not_shortest_label_en = Text("Path along latitude", font_size=12, color=YELLOW_A)
        not_shortest_group = VGroup(not_shortest_label, not_shortest_label_en).arrange(DOWN, buff=0.05)
        not_shortest_group.to_corner(UR, buff=0.3)
        self.add_fixed_in_frame_mobjects(not_shortest_group)

        self.play(
            Create(latitude_path),
            Write(not_shortest_group),
            run_time=1.2,
        )
        self.wait(0.5)

        # ===== 大圏コース（測地線・最短経路）=====
        def great_circle_path(t, p1, p2):
            """2点間の大圏に沿った補間（球面線形補間）"""
            omega = np.arccos(np.clip(np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2)), -1, 1))
            if omega < 1e-6:
                return p1
            return (np.sin((1 - t) * omega) * p1 + np.sin(t * omega) * p2) / np.sin(omega)

        p1_norm = point_A / np.linalg.norm(point_A)
        p2_norm = point_B / np.linalg.norm(point_B)

        great_circle = ParametricFunction(
            lambda t: sphere_radius * great_circle_path(t, p1_norm, p2_norm),
            t_range=[0, 1],
            color=ORANGE,
            stroke_width=5,
        )

        # ラベル更新
        shortest_label = Text("大圏コース（測地線）", font_size=18, color=ORANGE)
        shortest_label_en = Text("Great circle (Geodesic)", font_size=12, color=ORANGE)
        shortest_group = VGroup(shortest_label, shortest_label_en).arrange(DOWN, buff=0.05)
        shortest_group.to_corner(UR, buff=0.3)
        self.add_fixed_in_frame_mobjects(shortest_group)

        self.play(
            FadeOut(latitude_path),
            FadeOut(not_shortest_group),
            run_time=0.4,
        )
        self.play(
            Create(great_circle),
            FadeIn(shortest_group),
            run_time=1.5,
        )

        # カメラを少し回転させて大圏が北に膨らんでいることを強調
        self.move_camera(theta=-30 * DEGREES, run_time=1.5)
        self.wait(0.3)

        # ===== 説明テキスト =====
        explain1 = Text("北に膨らんで見えるけど...", font_size=20, color=WHITE)
        explain1_en = Text("Looks curved northward, but...", font_size=14, color=GRAY)
        explain_group1 = VGroup(explain1, explain1_en).arrange(DOWN, buff=0.05)
        explain_group1.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(explain_group1)

        self.play(Write(explain_group1), run_time=0.6)
        self.wait(0.8)

        explain2 = Text("これが最短経路！", font_size=24, color=ORANGE)
        explain2_en = Text("This IS the shortest path!", font_size=16, color=ORANGE)
        explain_group2 = VGroup(explain2, explain2_en).arrange(DOWN, buff=0.05)
        explain_group2.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(explain_group2)

        self.play(
            FadeOut(explain_group1),
            FadeIn(explain_group2),
            run_time=0.5,
        )
        self.wait(0.8)

        # ===== 結論 =====
        conclusion = Text("曲がった空間での「まっすぐ」= 測地線", font_size=22, color=WHITE)
        conclusion_en = Text('"Straight" in curved space = Geodesic', font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(conclusion_group)

        self.play(
            FadeOut(explain_group2),
            FadeIn(conclusion_group),
            run_time=0.6,
        )
        self.wait(1.5)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/spacetime_geodesic.py SpacetimeGeodesicConvergence")
    print("  manim -pql scripts/spacetime_geodesic.py SpacetimeGeodesicSimple")
    print("  manim -pql scripts/spacetime_geodesic.py SpacetimeGeodesicWithGeodesicLabel")
    print("  manim -pql scripts/spacetime_geodesic.py SpacetimeGeodesicComparison")
    print("  manim -pql scripts/spacetime_geodesic.py GeodesicShortestPath3D")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  SpacetimeGeodesicConvergence      - 基本版（時空図で測地線が収束）")
    print("                                      Basic version (geodesics converge in spacetime)")
    print("  SpacetimeGeodesicSimple           - シンプル版（最小構成）")
    print("                                      Simple version (minimal)")
    print("  SpacetimeGeodesicWithGeodesicLabel - 測地線ラベル付き版（L126への橋渡し）")
    print("                                       Geodesic label version (bridge to L126)")
    print("  SpacetimeGeodesicComparison       - 比較版（平坦 vs 曲がった時空）")
    print("                                      Comparison version (flat vs curved)")
    print("  GeodesicShortestPath3D            - 3D球面版（大圏コース・L126-128解説）")
    print("                                      3D sphere version (great circle, L126-128)")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
