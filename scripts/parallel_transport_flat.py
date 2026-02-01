"""
平坦な空間での平行移動
Parallel Transport in Flat Space

平坦な平面で下を向いたベクトルを正方形の格子の上を反時計回りで1周させ、
向きが変わらないことを示すアニメーション。

A vector pointing downward moves counterclockwise around a square grid
on a flat plane, showing that its direction remains unchanged.

yt_script.md L154-158 の解説用
目標時間: 25-30秒
"""

from manim import *
import numpy as np


class ParallelTransportFlat(Scene):
    """
    平坦な空間での平行移動アニメーション
    Parallel transport animation in flat space

    部屋の中で南を指差しながら歩いても、一周して戻ってきたら
    指は元の向きのまま、という直感的な説明のビジュアル化。

    Visualizing the intuitive explanation that if you walk around
    a room while pointing south, your finger still points the same
    direction when you return.
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("平坦な空間での平行移動", font_size=28)
        title_en = Text("Parallel Transport in Flat Space", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group), run_time=1.0)
        self.wait(0.5)

        # ===== 正方形の格子を作成 =====
        grid_size = 2.0  # 格子の半径
        num_lines = 9    # 格子線の数

        grid = VGroup()
        spacing = 2 * grid_size / (num_lines - 1)

        # 縦線
        for i in range(num_lines):
            x = -grid_size + spacing * i
            line = Line(
                UP * grid_size + RIGHT * x,
                DOWN * grid_size + RIGHT * x,
                color=BLUE_B,
                stroke_width=1.5,
                stroke_opacity=0.6,
            )
            grid.add(line)

        # 横線
        for i in range(num_lines):
            y = -grid_size + spacing * i
            line = Line(
                LEFT * grid_size + UP * y,
                RIGHT * grid_size + UP * y,
                color=BLUE_B,
                stroke_width=1.5,
                stroke_opacity=0.6,
            )
            grid.add(line)

        grid.shift(DOWN * 0.3)  # 少し下にずらす

        self.play(Create(grid), run_time=1.5)
        self.wait(0.5)

        # ===== 正方形の経路を設定 =====
        # 格子の内側に正方形の経路を設定
        path_size = 1.3
        center_offset = DOWN * 0.3

        # 正方形の角（反時計回り）
        corners = [
            center_offset + np.array([-path_size, -path_size, 0]),  # 左下（開始点）
            center_offset + np.array([path_size, -path_size, 0]),   # 右下
            center_offset + np.array([path_size, path_size, 0]),    # 右上
            center_offset + np.array([-path_size, path_size, 0]),   # 左上
        ]

        # 経路を可視化（点線）
        path_lines = VGroup()
        for i in range(4):
            start = corners[i]
            end = corners[(i + 1) % 4]
            path_line = DashedLine(
                start, end,
                color=YELLOW_A,
                stroke_width=2,
                dash_length=0.15,
            )
            path_lines.add(path_line)

        self.play(Create(path_lines), run_time=1.0)
        self.wait(0.3)

        # ===== ベクトル（矢印）を作成 =====
        # 下向きのベクトル（南を指す）
        vector_length = 0.7

        def create_vector_at(position, direction=DOWN):
            """指定位置にベクトルを作成"""
            arrow = Arrow(
                position,
                position + direction * vector_length,
                color=RED,
                stroke_width=4,
                buff=0,
                max_tip_length_to_length_ratio=0.25,
            )
            return arrow

        # 開始位置（左下）にベクトルを配置
        start_pos = corners[0]
        vector = create_vector_at(start_pos, DOWN)

        # 方位を示すテキスト
        direction_text = Text("南 / South", font_size=16, color=RED_A)
        direction_text.next_to(vector, RIGHT, buff=0.3)

        self.play(
            GrowArrow(vector),
            Write(direction_text),
            run_time=0.8,
        )
        self.wait(0.5)

        # ===== 「方向を保ったまま移動」のテキスト =====
        move_text = Text("方向を保ったまま移動", font_size=18, color=WHITE)
        move_text_en = Text("Move while keeping direction", font_size=12, color=GRAY)
        move_text_group = VGroup(move_text, move_text_en).arrange(DOWN, buff=0.05)
        move_text_group.to_edge(DOWN, buff=0.4)

        self.play(Write(move_text_group), run_time=0.6)
        self.wait(0.5)

        # ===== 正方形の経路を反時計回りに移動 =====
        # 各辺の移動時間（25-30秒目標のため、ゆっくり移動）
        edge_time = 1.8

        # 辺1: 左下 → 右下
        self.play(
            vector.animate.move_to(corners[1] + DOWN * vector_length / 2),
            direction_text.animate.next_to(corners[1] + DOWN * vector_length / 2, RIGHT, buff=0.3),
            run_time=edge_time,
            rate_func=linear,
        )

        # 辺2: 右下 → 右上
        self.play(
            vector.animate.move_to(corners[2] + DOWN * vector_length / 2),
            direction_text.animate.next_to(corners[2] + DOWN * vector_length / 2, RIGHT, buff=0.3),
            run_time=edge_time,
            rate_func=linear,
        )

        # 辺3: 右上 → 左上
        self.play(
            vector.animate.move_to(corners[3] + DOWN * vector_length / 2),
            direction_text.animate.next_to(corners[3] + DOWN * vector_length / 2, RIGHT, buff=0.3),
            run_time=edge_time,
            rate_func=linear,
        )

        # 辺4: 左上 → 左下（開始点に戻る）
        self.play(
            vector.animate.move_to(start_pos + DOWN * vector_length / 2),
            direction_text.animate.next_to(start_pos + DOWN * vector_length / 2, RIGHT, buff=0.3),
            run_time=edge_time,
            rate_func=linear,
        )

        self.wait(0.5)

        # ===== 結果の強調 =====
        # 「向きは変わらない」を強調
        result_text = Text("一周しても向きは変わらない！", font_size=22, color=YELLOW)
        result_text_en = Text("Direction unchanged after one loop!", font_size=14, color=YELLOW_A)
        result_text_group = VGroup(result_text, result_text_en).arrange(DOWN, buff=0.08)
        result_text_group.to_edge(DOWN, buff=0.4)

        # ベクトルをフラッシュさせる
        flash_circle = Circle(radius=0.5, color=YELLOW, fill_opacity=0.3)
        flash_circle.move_to(vector.get_center())

        self.play(
            Transform(move_text_group, result_text_group),
            GrowFromCenter(flash_circle),
            run_time=0.6,
        )
        self.play(
            flash_circle.animate.scale(1.5).set_opacity(0),
            run_time=0.5,
        )
        self.remove(flash_circle)

        self.wait(0.5)

        # ===== 「これは当たり前」のメッセージ =====
        obvious_text = Text("平坦な空間では当たり前", font_size=20, color=WHITE)
        obvious_text_en = Text("Obvious in flat space", font_size=14, color=GRAY)
        obvious_text_group = VGroup(obvious_text, obvious_text_en).arrange(DOWN, buff=0.08)
        obvious_text_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(move_text_group, obvious_text_group), run_time=0.6)
        self.wait(1.0)

        # ===== 次への伏線 =====
        next_text = Text("では、曲がった空間では…？", font_size=22, color=GREEN)
        next_text_en = Text("But in curved space...?", font_size=14, color=GREEN_A)
        next_text_group = VGroup(next_text, next_text_en).arrange(DOWN, buff=0.08)
        next_text_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(move_text_group, next_text_group), run_time=0.7)
        self.wait(2.0)


class ParallelTransportFlatWithTrace(Scene):
    """
    軌跡付き版：移動経路を線で追跡
    Version with trace: Track the movement path with a line
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("平坦な空間での平行移動", font_size=28)
        title_en = Text("Parallel Transport in Flat Space", font_size=18, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group), run_time=0.8)
        self.wait(0.2)

        # ===== 格子 =====
        grid_size = 2.0
        num_lines = 9
        grid = VGroup()
        spacing = 2 * grid_size / (num_lines - 1)

        for i in range(num_lines):
            x = -grid_size + spacing * i
            grid.add(Line(
                UP * grid_size + RIGHT * x,
                DOWN * grid_size + RIGHT * x,
                color=BLUE_B, stroke_width=1.5, stroke_opacity=0.5,
            ))
        for i in range(num_lines):
            y = -grid_size + spacing * i
            grid.add(Line(
                LEFT * grid_size + UP * y,
                RIGHT * grid_size + UP * y,
                color=BLUE_B, stroke_width=1.5, stroke_opacity=0.5,
            ))

        grid.shift(DOWN * 0.3)
        self.play(Create(grid), run_time=0.8)

        # ===== 経路設定 =====
        path_size = 1.3
        center_offset = DOWN * 0.3
        corners = [
            center_offset + np.array([-path_size, -path_size, 0]),
            center_offset + np.array([path_size, -path_size, 0]),
            center_offset + np.array([path_size, path_size, 0]),
            center_offset + np.array([-path_size, path_size, 0]),
        ]

        # ===== ベクトル =====
        vector_length = 0.7
        start_pos = corners[0]

        # ベクトルの根元を示すドット
        base_dot = Dot(start_pos, radius=0.08, color=ORANGE)

        # ベクトル
        vector = Arrow(
            start_pos,
            start_pos + DOWN * vector_length,
            color=RED,
            stroke_width=4,
            buff=0,
            max_tip_length_to_length_ratio=0.25,
        )

        self.play(
            FadeIn(base_dot),
            GrowArrow(vector),
            run_time=0.5,
        )

        # ===== 説明テキスト =====
        text = Text("「南」を指したまま歩く", font_size=18, color=WHITE)
        text_en = Text('Walking while pointing "south"', font_size=12, color=GRAY)
        text_group = VGroup(text, text_en).arrange(DOWN, buff=0.05)
        text_group.to_edge(DOWN, buff=0.4)

        self.play(Write(text_group), run_time=0.5)
        self.wait(0.3)

        # ===== 軌跡を追加するためのTracedPath =====
        traced_path = TracedPath(
            base_dot.get_center,
            stroke_color=YELLOW,
            stroke_width=3,
        )
        self.add(traced_path)

        # ===== 移動（4辺を連続で） =====
        total_time = 5.0
        edge_time = total_time / 4

        for i in range(4):
            next_corner = corners[(i + 1) % 4]
            self.play(
                base_dot.animate.move_to(next_corner),
                vector.animate.move_to(next_corner + DOWN * vector_length / 2),
                run_time=edge_time,
                rate_func=linear,
            )

        self.wait(0.3)

        # ===== 結果 =====
        result_text = Text("一周しても向きは同じ！", font_size=22, color=YELLOW)
        result_text_en = Text("Same direction after one loop!", font_size=14, color=YELLOW_A)
        result_text_group = VGroup(result_text, result_text_en).arrange(DOWN, buff=0.08)
        result_text_group.to_edge(DOWN, buff=0.4)

        # フラッシュ効果
        flash = Circle(radius=0.5, color=YELLOW, fill_opacity=0.4)
        flash.move_to(vector.get_center())

        self.play(
            Transform(text_group, result_text_group),
            GrowFromCenter(flash),
            run_time=0.4,
        )
        self.play(
            flash.animate.scale(2).set_opacity(0),
            run_time=0.3,
        )
        self.remove(flash)

        self.wait(0.5)

        # ===== 次への伏線 =====
        next_text = Text("では、地球の表面では…？", font_size=22, color=GREEN)
        next_text_en = Text("But on Earth's surface...?", font_size=14, color=GREEN_A)
        next_text_group = VGroup(next_text, next_text_en).arrange(DOWN, buff=0.08)
        next_text_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(text_group, next_text_group), run_time=0.5)
        self.wait(1.5)


class ParallelTransportFlatRoom(Scene):
    """
    部屋バージョン：より直感的な「部屋の中を歩く」表現
    Room version: More intuitive "walking in a room" representation
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("部屋の中で「南」を指差しながら歩く", font_size=26)
        title_en = Text('Walking while pointing "south" in a room', font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        self.play(Write(title_group), run_time=0.8)
        self.wait(0.2)

        # ===== 部屋を表現（床のタイル） =====
        room_size = 2.2
        num_tiles = 6
        room = VGroup()
        tile_size = 2 * room_size / num_tiles

        for i in range(num_tiles):
            for j in range(num_tiles):
                x = -room_size + tile_size * (i + 0.5)
                y = -room_size + tile_size * (j + 0.5)
                tile = Square(
                    side_length=tile_size * 0.95,
                    color=BLUE_B,
                    stroke_width=1.5,
                    fill_opacity=0.1,
                )
                tile.move_to(np.array([x, y, 0]))
                room.add(tile)

        room.shift(DOWN * 0.3)

        # 壁を示す外枠
        room_border = Square(
            side_length=2 * room_size,
            color=WHITE,
            stroke_width=3,
        )
        room_border.shift(DOWN * 0.3)

        self.play(
            Create(room),
            Create(room_border),
            run_time=1.0,
        )

        # ===== 方位を示すコンパス =====
        compass_center = RIGHT * 3 + UP * 2
        compass_size = 0.6

        compass = VGroup()
        # Nマーカー
        n_text = Text("N", font_size=14, color=WHITE)
        n_text.move_to(compass_center + UP * compass_size)
        # Sマーカー
        s_text = Text("S", font_size=14, color=RED_A)
        s_text.move_to(compass_center + DOWN * compass_size)
        # 矢印（南向き）
        compass_arrow = Arrow(
            compass_center + UP * 0.2,
            compass_center + DOWN * 0.3,
            color=RED,
            stroke_width=3,
            buff=0,
        )
        compass.add(n_text, s_text, compass_arrow)

        self.play(FadeIn(compass), run_time=0.4)
        self.wait(0.2)

        # ===== 人を示すドットとベクトル =====
        path_size = 1.4
        center_offset = DOWN * 0.3
        corners = [
            center_offset + np.array([-path_size, -path_size, 0]),
            center_offset + np.array([path_size, -path_size, 0]),
            center_offset + np.array([path_size, path_size, 0]),
            center_offset + np.array([-path_size, path_size, 0]),
        ]

        # 人を示すドット
        person = Dot(corners[0], radius=0.12, color=ORANGE)

        # 指差すベクトル（南向き）
        vector_length = 0.6
        pointing = Arrow(
            corners[0],
            corners[0] + DOWN * vector_length,
            color=RED,
            stroke_width=4,
            buff=0,
            max_tip_length_to_length_ratio=0.3,
        )

        self.play(
            FadeIn(person, scale=0.5),
            GrowArrow(pointing),
            run_time=0.5,
        )
        self.wait(0.3)

        # ===== 歩行経路（点線） =====
        path_lines = VGroup()
        for i in range(4):
            path_line = DashedLine(
                corners[i],
                corners[(i + 1) % 4],
                color=YELLOW_A,
                stroke_width=2,
                dash_length=0.12,
            )
            path_lines.add(path_line)

        self.play(Create(path_lines), run_time=0.6)

        # ===== 説明テキスト =====
        walk_text = Text("ぐるっと一周", font_size=18, color=WHITE)
        walk_text_en = Text("Walk around", font_size=12, color=GRAY)
        walk_text_group = VGroup(walk_text, walk_text_en).arrange(DOWN, buff=0.05)
        walk_text_group.to_edge(DOWN, buff=0.4)

        self.play(Write(walk_text_group), run_time=0.4)
        self.wait(0.2)

        # ===== 移動アニメーション =====
        total_time = 5.0
        edge_time = total_time / 4

        for i in range(4):
            next_corner = corners[(i + 1) % 4]
            self.play(
                person.animate.move_to(next_corner),
                pointing.animate.move_to(next_corner + DOWN * vector_length / 2),
                run_time=edge_time,
                rate_func=linear,
            )

        self.wait(0.3)

        # ===== 結果 =====
        result_text = Text("指は南を向いたまま！", font_size=22, color=YELLOW)
        result_text_en = Text("Finger still points south!", font_size=14, color=YELLOW_A)
        result_text_group = VGroup(result_text, result_text_en).arrange(DOWN, buff=0.08)
        result_text_group.to_edge(DOWN, buff=0.4)

        # 強調エフェクト
        flash = Circle(radius=0.4, color=YELLOW, fill_opacity=0.4)
        flash.move_to(pointing.get_center())

        self.play(
            Transform(walk_text_group, result_text_group),
            GrowFromCenter(flash),
            run_time=0.4,
        )
        self.play(
            flash.animate.scale(2).set_opacity(0),
            run_time=0.3,
        )
        self.remove(flash)

        self.wait(0.5)

        # ===== 「当たり前」メッセージ =====
        obvious_text = Text("これは当たり前…", font_size=20, color=WHITE)
        obvious_text_en = Text("This is obvious...", font_size=14, color=GRAY)
        obvious_text_group = VGroup(obvious_text, obvious_text_en).arrange(DOWN, buff=0.08)
        obvious_text_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(walk_text_group, obvious_text_group), run_time=0.5)
        self.wait(0.5)

        # ===== 次への伏線 =====
        next_text = Text("では、地球の表面で同じことをすると…？", font_size=20, color=GREEN)
        next_text_en = Text("But what if we do the same on Earth's surface...?", font_size=12, color=GREEN_A)
        next_text_group = VGroup(next_text, next_text_en).arrange(DOWN, buff=0.08)
        next_text_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(walk_text_group, next_text_group), run_time=0.6)
        self.wait(1.5)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/parallel_transport_flat.py ParallelTransportFlat")
    print("  manim -pql scripts/parallel_transport_flat.py ParallelTransportFlatWithTrace")
    print("  manim -pql scripts/parallel_transport_flat.py ParallelTransportFlatRoom")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  ParallelTransportFlat       - 基本版（格子上の平行移動）")
    print("                                Basic version (parallel transport on grid)")
    print("  ParallelTransportFlatWithTrace - 軌跡付き版（移動経路を表示）")
    print("                                   Version with trace (show movement path)")
    print("  ParallelTransportFlatRoom   - 部屋バージョン（より直感的な表現）")
    print("                                Room version (more intuitive)")
