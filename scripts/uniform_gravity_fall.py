"""
平坦な空間（一様な重力場）でのボール落下アニメーション

横に並べた2つのボールが平行に落下し、
同時に地面に到着して静止する様子を可視化します。

これは「直感的な予想」を表現するアニメーションで、
後に曲がった時空（非一様重力場）との対比に使用します。
"""

from manim import *


class UniformGravityFall(Scene):
    """一様重力場でのボール落下アニメーション"""

    def construct(self):
        # 地面を作成（塗りつぶし）
        ground = Rectangle(
            width=14,
            height=1.5,
            color=DARK_BROWN,
            fill_opacity=1.0,
        )
        ground.set_stroke(color=LIGHT_BROWN, width=3)
        ground.move_to(DOWN * 3)

        # 地面の上面ライン（より明確に）
        ground_line = Line(
            LEFT * 7 + DOWN * 2.25,
            RIGHT * 7 + DOWN * 2.25,
            color=LIGHT_BROWN,
            stroke_width=4,
        )

        # ボールを作成（アウトライン付き）
        ball_radius = 0.4
        ball_spacing = 2.0  # ボール間の距離
        start_height = 2.5  # 開始位置の高さ

        # 左のボール（赤系）
        ball_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.8)
        ball_left.set_stroke(color=RED_A, width=4)
        ball_left.move_to(LEFT * (ball_spacing / 2) + UP * start_height)

        # 右のボール（青系）
        ball_right = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.8)
        ball_right.set_stroke(color=BLUE_A, width=4)
        ball_right.move_to(RIGHT * (ball_spacing / 2) + UP * start_height)

        # 初期位置の水平破線（同じ高さを明示）
        start_line = DashedLine(
            LEFT * 4 + UP * start_height,
            RIGHT * 4 + UP * start_height,
            color=GRAY,
            stroke_width=2,
            dash_length=0.2,
        )

        # 地面に着地した時のy座標（ボールの半径分上）
        landing_y = -2.25 + ball_radius

        # シーンの構築
        # 地面を表示
        self.play(FadeIn(ground), Create(ground_line))
        self.wait(0.3)

        # 初期位置の破線を表示
        self.play(Create(start_line))
        self.wait(0.2)

        # ボールを表示
        self.play(
            GrowFromCenter(ball_left),
            GrowFromCenter(ball_right),
        )
        self.wait(0.5)

        # 落下アニメーション
        # 一様重力場では等加速度運動（rate_func で表現）
        fall_duration = 1.5

        self.play(
            ball_left.animate.move_to(
                LEFT * (ball_spacing / 2) + UP * landing_y
            ),
            ball_right.animate.move_to(
                RIGHT * (ball_spacing / 2) + UP * landing_y
            ),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,  # 加速度運動を模倣
        )

        # 着地の小さなバウンス効果
        bounce_height = 0.15
        self.play(
            ball_left.animate.shift(UP * bounce_height),
            ball_right.animate.shift(UP * bounce_height),
            run_time=0.1,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            ball_left.animate.shift(DOWN * bounce_height),
            ball_right.animate.shift(DOWN * bounce_height),
            run_time=0.1,
            rate_func=rate_functions.ease_in_quad,
        )

        # 静止状態で待機
        self.wait(1.5)


class UniformGravityFallWithLabel(Scene):
    """一様重力場でのボール落下（ラベル付き）"""

    def construct(self):
        # タイトル
        title = Text("平坦な空間（一様な重力場）", font_size=32)
        title.to_edge(UP)

        # 地面を作成
        ground = Rectangle(
            width=14,
            height=1.5,
            color=DARK_BROWN,
            fill_opacity=1.0,
        )
        ground.set_stroke(color=LIGHT_BROWN, width=3)
        ground.move_to(DOWN * 3)

        ground_line = Line(
            LEFT * 7 + DOWN * 2.25,
            RIGHT * 7 + DOWN * 2.25,
            color=LIGHT_BROWN,
            stroke_width=4,
        )

        # ボールを作成
        ball_radius = 0.4
        ball_spacing = 2.0
        start_height = 2.0

        ball_left = Circle(radius=ball_radius, color=RED_C, fill_opacity=0.8)
        ball_left.set_stroke(color=RED_A, width=4)
        ball_left.move_to(LEFT * (ball_spacing / 2) + UP * start_height)

        ball_right = Circle(radius=ball_radius, color=BLUE_C, fill_opacity=0.8)
        ball_right.set_stroke(color=BLUE_A, width=4)
        ball_right.move_to(RIGHT * (ball_spacing / 2) + UP * start_height)

        # 初期位置の水平破線（同じ高さを明示）
        start_line = DashedLine(
            LEFT * 4 + UP * start_height,
            RIGHT * 4 + UP * start_height,
            color=GRAY,
            stroke_width=2,
            dash_length=0.2,
        )

        landing_y = -2.25 + ball_radius

        # ボール間の距離を示す両矢印
        distance_line = DoubleArrow(
            ball_left.get_center() + DOWN * 0.6,
            ball_right.get_center() + DOWN * 0.6,
            color=YELLOW,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.1,
        )
        distance_label = Text("一定", font_size=20, color=YELLOW)
        distance_label.next_to(distance_line, DOWN, buff=0.1)

        # シーンの構築
        self.play(Write(title))
        self.play(FadeIn(ground), Create(ground_line))
        self.wait(0.2)

        # 初期位置の破線を表示
        self.play(Create(start_line))
        self.wait(0.2)

        self.play(
            GrowFromCenter(ball_left),
            GrowFromCenter(ball_right),
        )
        self.wait(0.3)

        # 距離を示す
        self.play(
            GrowFromCenter(distance_line),
            FadeIn(distance_label),
        )
        self.wait(0.5)

        # 落下アニメーション（距離表示も一緒に動く）
        fall_duration = 1.5
        final_left_pos = LEFT * (ball_spacing / 2) + UP * landing_y
        final_right_pos = RIGHT * (ball_spacing / 2) + UP * landing_y

        self.play(
            ball_left.animate.move_to(final_left_pos),
            ball_right.animate.move_to(final_right_pos),
            distance_line.animate.move_to(
                (final_left_pos + final_right_pos) / 2 + DOWN * 0.6
            ),
            distance_label.animate.move_to(
                (final_left_pos + final_right_pos) / 2 + DOWN * 0.9
            ),
            run_time=fall_duration,
            rate_func=rate_functions.ease_in_quad,
        )

        # バウンス
        bounce_height = 0.15
        self.play(
            ball_left.animate.shift(UP * bounce_height),
            ball_right.animate.shift(UP * bounce_height),
            run_time=0.1,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            ball_left.animate.shift(DOWN * bounce_height),
            ball_right.animate.shift(DOWN * bounce_height),
            run_time=0.1,
            rate_func=rate_functions.ease_in_quad,
        )

        # 結果テキスト
        result_text = Text(
            "平行に落ちて、同時に着地",
            font_size=28,
            color=GREEN,
        )
        result_text.next_to(title, DOWN, buff=0.3)

        self.play(Write(result_text))
        self.wait(2)


class UniformGravityFallSimple(Scene):
    """シンプル版：一様重力場でのボール落下"""

    def construct(self):
        # 地面を作成（塗りつぶし）
        ground = Rectangle(
            width=14,
            height=1.2,
            color="#4a3728",  # ダークブラウン
            fill_opacity=1.0,
        )
        ground.set_stroke(color="#8b7355", width=3)  # ライトブラウン
        ground.move_to(DOWN * 3.1)

        # ボールを作成（アウトライン付き）
        ball_radius = 0.45
        ball_spacing = 2.5
        start_height = 2.5

        ball_left = Circle(radius=ball_radius, color="#e74c3c", fill_opacity=0.85)
        ball_left.set_stroke(color="#ffffff", width=3)
        ball_left.move_to(LEFT * (ball_spacing / 2) + UP * start_height)

        ball_right = Circle(radius=ball_radius, color="#3498db", fill_opacity=0.85)
        ball_right.set_stroke(color="#ffffff", width=3)
        ball_right.move_to(RIGHT * (ball_spacing / 2) + UP * start_height)

        # 初期位置の水平破線（同じ高さを明示）
        start_line = DashedLine(
            LEFT * 4 + UP * start_height,
            RIGHT * 4 + UP * start_height,
            color=GRAY,
            stroke_width=2,
            dash_length=0.2,
        )

        landing_y = -3.1 + 0.6 + ball_radius  # 地面上面 + ボール半径

        # 地面を表示
        self.add(ground)
        self.wait(0.2)

        # 初期位置の破線を表示
        self.play(Create(start_line), run_time=0.3)

        # ボールを表示
        self.play(
            FadeIn(ball_left, scale=0.5),
            FadeIn(ball_right, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.3)

        # 落下アニメーション
        self.play(
            ball_left.animate.move_to(LEFT * (ball_spacing / 2) + UP * landing_y),
            ball_right.animate.move_to(RIGHT * (ball_spacing / 2) + UP * landing_y),
            run_time=1.2,
            rate_func=rate_functions.ease_in_quad,
        )

        # 軽いバウンス
        self.play(
            ball_left.animate.shift(UP * 0.1),
            ball_right.animate.shift(UP * 0.1),
            run_time=0.08,
        )
        self.play(
            ball_left.animate.shift(DOWN * 0.1),
            ball_right.animate.shift(DOWN * 0.1),
            run_time=0.08,
        )

        # 静止
        self.wait(1.5)


if __name__ == "__main__":
    # コマンドラインから実行する場合のヘルプ
    print("使用方法:")
    print("  manim -pql scripts/uniform_gravity_fall.py UniformGravityFall")
    print("  manim -pql scripts/uniform_gravity_fall.py UniformGravityFallWithLabel")
    print("  manim -pql scripts/uniform_gravity_fall.py UniformGravityFallSimple")
    print("")
    print("シーン説明:")
    print("  UniformGravityFall      - 基本版（地面とボールのみ）")
    print("  UniformGravityFallWithLabel - ラベル付き版（タイトル・距離表示あり）")
    print("  UniformGravityFallSimple    - シンプル版（最小構成）")
    print("")
    print("オプション:")
    print("  -p: プレビュー（再生）")
    print("  -ql: 低品質（高速）")
    print("  -qm: 中品質")
    print("  -qh: 高品質")
    print("  -qk: 4K品質")
