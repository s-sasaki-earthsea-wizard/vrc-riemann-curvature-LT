"""
体が潮汐力で引き伸ばされるアニメーション
Body being stretched by tidal forces

椅子に座った人の頭と足で重力の大きさが異なり、
その結果、体が縦に引き伸ばされ、横に圧縮されることを示す。

脚本L11-15に対応：
「重力による時空の曲がりの効果は、あなたの体にも起きています。」
「あなたが今、椅子に座ってこの動画を見ているとしましょう...」
「足の方が地球に近いので、ほんの少しだけ強い重力を受けて、」
「その結果、あなたの体は縦に少し引き伸ばされているんです。」
"""

from manim import *
import os


def create_text_with_backplate(text_content, font_size, text_color, bg_color="#000000", bg_opacity=0.7, padding=0.15):
    """
    バックプレート付きテキストを作成するヘルパー関数
    Helper function to create text with a background plate
    """
    text = Text(text_content, font_size=font_size, color=text_color)
    # バックプレート（背景矩形）を作成
    # Create background rectangle
    backplate = Rectangle(
        width=text.width + padding * 2,
        height=text.height + padding * 2,
        color=bg_color,
        fill_color=bg_color,
        fill_opacity=bg_opacity,
        stroke_width=0,
    )
    backplate.move_to(text.get_center())
    # グループ化して返す
    # Group and return
    return VGroup(backplate, text)


class TidalStretchBody(Scene):
    """潮汐力による体の引き伸ばし / Body stretching due to tidal forces"""

    def construct(self):
        # 背景色を設定（暗めの色で画像が映えるように）
        # Set background color (darker to make image stand out)
        self.camera.background_color = "#1a1a2e"

        # 椅子に座ったアバター画像を読み込む
        # Load sitting avatar image
        script_dir = os.path.dirname(os.path.abspath(__file__))
        avatar_path = os.path.join(script_dir, "assets", "sitting-avatar.png")
        avatar = ImageMobject(avatar_path)

        # 画像の縦方向が画面全域に入るようにスケール調整
        # Scale to fit the full vertical extent of the screen
        # Manimのデフォルトフレームは縦8ユニット（-4〜+4）
        target_height = 6.5  # 上下に余白を残す
        avatar.scale_to_fit_height(target_height)
        avatar.move_to(LEFT * 3.0)  # 左側に配置してテキスト用スペースを確保

        # 地球を示す弧（画面下部）
        # Arc representing Earth (bottom of screen)
        earth_arc = Arc(
            radius=15,
            start_angle=PI * 0.38,
            angle=PI * 0.24,
            color="#3498db",
            stroke_width=10,
        )
        earth_arc.move_to(DOWN * 12)

        # 地球のラベル（バックプレート付き）
        # Earth label (with backplate)
        earth_label = create_text_with_backplate(
            "↓ 地球 / Earth ↓", font_size=22, text_color="#3498db"
        )
        earth_label.move_to(DOWN * 3.6)

        # --- フェーズ1: アバターと地球を表示 ---
        # --- Phase 1: Show avatar and Earth ---
        self.play(
            FadeIn(avatar, scale=0.9),
            run_time=0.8,
        )
        self.play(
            Create(earth_arc),
            FadeIn(earth_label),
            run_time=0.6,
        )
        self.wait(0.5)

        # --- フェーズ2: 頭と足で重力の矢印を表示（長さが異なる） ---
        # --- Phase 2: Show gravity arrows at head and feet (different lengths) ---

        # アバターの頭と足の位置を取得
        # Get head and feet positions of avatar
        head_pos = avatar.get_top()
        feet_pos = avatar.get_bottom()
        avatar_center = avatar.get_center()

        # 頭への重力（短い矢印）
        # Gravity on head (shorter arrow)
        gravity_head = Arrow(
            start=head_pos + LEFT * 0.8,
            end=head_pos + LEFT * 0.8 + DOWN * 0.9,
            color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.35,
            buff=0,
        )

        # 足への重力（長い矢印）- 画面内に収まるよう調整
        # Gravity on feet (longer arrow) - adjusted to stay within frame
        gravity_feet = Arrow(
            start=feet_pos + LEFT * 0.8 + UP * 0.6,
            end=feet_pos + LEFT * 0.8 + UP * 0.6 + DOWN * 1.25,
            color=ORANGE,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

        # 重力ラベル（バックプレート付き）
        # Gravity labels (with backplate)
        gravity_head_label = create_text_with_backplate(
            "g（弱）/ g (weak)", font_size=18, text_color=YELLOW
        )
        gravity_head_label.next_to(gravity_head, LEFT, buff=0.15)

        gravity_feet_label = create_text_with_backplate(
            "g（強）/ g (strong)", font_size=18, text_color=ORANGE
        )
        gravity_feet_label.next_to(gravity_feet, LEFT, buff=0.1)

        # 説明テキスト（バックプレート付き）
        # Explanation text (with backplate)
        explanation_text = create_text_with_backplate(
            "頭と足では\n地球からの距離が違う\n→ 重力の強さが違う",
            font_size=24,
            text_color=WHITE,
            bg_opacity=0.8,
        )
        explanation_text.move_to(RIGHT * 3.0 + UP * 2.0)

        explanation_text_en = create_text_with_backplate(
            "Head and feet are at\ndifferent distances from Earth\n→ Different gravity strength",
            font_size=20,
            text_color=GRAY_B,
            bg_opacity=0.8,
        )
        explanation_text_en.next_to(explanation_text, DOWN, buff=0.3)

        self.play(
            GrowArrow(gravity_head),
            GrowArrow(gravity_feet),
            run_time=0.7,
        )
        self.play(
            FadeIn(gravity_head_label),
            FadeIn(gravity_feet_label),
            run_time=0.5,
        )
        self.play(
            FadeIn(explanation_text),
            FadeIn(explanation_text_en),
            run_time=0.7,
        )
        self.wait(1.5)

        # --- フェーズ3: 潮汐力の効果を表示（縦に伸び、横に縮む） ---
        # --- Phase 3: Show tidal force effect (stretch vertically, compress horizontally) ---

        # 重力矢印と説明を消す
        # Remove gravity arrows and explanation
        self.play(
            FadeOut(gravity_head),
            FadeOut(gravity_feet),
            FadeOut(gravity_head_label),
            FadeOut(gravity_feet_label),
            FadeOut(explanation_text),
            FadeOut(explanation_text_en),
            run_time=0.5,
        )

        # 潮汐力を示す矢印（両方下向き、長さが異なる）
        # Tidal force arrows (both pointing down, different lengths)
        # 頭への重力（短い矢印）
        # Gravity on head (shorter arrow)
        tidal_head = Arrow(
            start=head_pos + LEFT * 0.8,
            end=head_pos + LEFT * 0.8 + DOWN * 0.7,
            color=RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )
        # 足への重力（長い矢印）
        # Gravity on feet (longer arrow)
        tidal_feet = Arrow(
            start=feet_pos + LEFT * 0.8 + UP * 0.5,
            end=feet_pos + LEFT * 0.8 + UP * 0.5 + DOWN * 1.2,
            color=RED,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )

        # 横方向の圧縮矢印（左右から地球中心に向かって斜め下に引かれる）
        # Compression arrows (pulled diagonally toward Earth's center from sides)
        # 地球中心は足元の遥か下にあるので、矢印は斜め下を向く
        # Earth's center is far below the feet, so arrows point diagonally downward
        compress_left = Arrow(
            start=avatar.get_left() + LEFT * 0.6 + UP * 0.3,
            end=avatar.get_left() + RIGHT * 0.1 + DOWN * 0.5,
            color=BLUE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )
        compress_right = Arrow(
            start=avatar.get_right() + RIGHT * 0.6 + UP * 0.3,
            end=avatar.get_right() + LEFT * 0.1 + DOWN * 0.5,
            color=BLUE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.4,
            buff=0,
        )

        # 潮汐力の説明（バックプレート付き）
        # Tidal force explanation (with backplate)
        tidal_explanation = create_text_with_backplate(
            "潮汐力の効果",
            font_size=28,
            text_color=WHITE,
            bg_opacity=0.85,
        )
        tidal_explanation.move_to(RIGHT * 3.0 + UP * 2.5)

        stretch_label = create_text_with_backplate(
            "重力の差 → 引き伸ばし\nGravity difference → Stretching",
            font_size=22,
            text_color=RED,
            bg_opacity=0.85,
        )
        stretch_label.move_to(RIGHT * 3.0 + UP * 1.0)

        compress_label = create_text_with_backplate(
            "地球中心へ引かれ圧縮\nPulled toward Earth's center",
            font_size=22,
            text_color=BLUE,
            bg_opacity=0.85,
        )
        compress_label.move_to(RIGHT * 3.0 + DOWN * 0.5)

        # 縦方向の矢印を表示
        # Show vertical arrows
        self.play(
            FadeIn(tidal_explanation),
            run_time=0.5,
        )
        self.play(
            GrowArrow(tidal_head),
            GrowArrow(tidal_feet),
            FadeIn(stretch_label),
            run_time=0.6,
        )

        # 横方向の矢印を表示
        # Show horizontal arrows
        self.play(
            GrowArrow(compress_left),
            GrowArrow(compress_right),
            FadeIn(compress_label),
            run_time=0.6,
        )

        self.wait(0.5)

        # アバターを引き伸ばし＆圧縮するアニメーション（誇張表現）
        # Stretch and compress avatar animation (exaggerated)
        self.play(
            avatar.animate.stretch(1.10, dim=1).stretch(0.92, dim=0),  # 縦10%伸び、横8%縮む
            tidal_head.animate.shift(DOWN * 0.15),
            tidal_feet.animate.shift(DOWN * 0.25),
            compress_left.animate.shift(RIGHT * 0.1 + DOWN * 0.1),
            compress_right.animate.shift(LEFT * 0.1 + DOWN * 0.1),
            run_time=1.0,
            rate_func=rate_functions.ease_out_quad,
        )

        self.wait(0.5)

        # --- フェーズ4: 注釈と潮汐力ラベル ---
        # --- Phase 4: Note and tidal force label ---

        # 注釈（効果は目に見えないほど小さい）
        # Note (effect is too small to see)
        note_text = create_text_with_backplate(
            "※実際の効果は目に見えないほど小さい\n* The actual effect is imperceptibly small",
            font_size=16,
            text_color=GRAY,
            bg_opacity=0.8,
        )
        note_text.move_to(RIGHT * 3.0 + DOWN * 2.0)

        # 潮汐力のラベル
        # Tidal force label
        tidal_label = create_text_with_backplate(
            "これが「潮汐力」\nThis is the \"Tidal Force\"",
            font_size=28,
            text_color=YELLOW,
            bg_opacity=0.9,
        )
        tidal_label.move_to(RIGHT * 3.0 + DOWN * 3.2)

        self.play(FadeIn(note_text), run_time=0.4)
        self.play(FadeIn(tidal_label), run_time=0.6)

        # 潮汐力ラベルを強調
        # Emphasize tidal force label
        self.play(
            tidal_label.animate.scale(1.1),
            run_time=0.25,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            tidal_label.animate.scale(1 / 1.1),
            run_time=0.25,
            rate_func=rate_functions.ease_in_quad,
        )

        # 静止
        # Hold
        self.wait(2.0)


class TidalStretchBodySimple(Scene):
    """シンプル版：潮汐力による体の引き伸ばし / Simple version: Body stretching due to tidal forces"""

    def construct(self):
        # 背景色
        self.camera.background_color = "#1a1a2e"

        # アバター画像を読み込む
        script_dir = os.path.dirname(os.path.abspath(__file__))
        avatar_path = os.path.join(script_dir, "assets", "sitting-avatar.png")
        avatar = ImageMobject(avatar_path)

        # 画像の縦方向が画面全域に入るようにスケール調整
        target_height = 6.0
        avatar.scale_to_fit_height(target_height)
        avatar.move_to(LEFT * 1.5)

        # アバターを表示
        self.play(FadeIn(avatar, scale=0.9), run_time=0.6)
        self.wait(0.3)

        # 重力矢印を表示（頭：短、足：長）
        head_pos = avatar.get_top()
        feet_pos = avatar.get_bottom()

        gravity_head = Arrow(
            start=head_pos + RIGHT * 1.0,
            end=head_pos + RIGHT * 1.0 + DOWN * 0.8,
            color=YELLOW,
            stroke_width=5,
            buff=0,
        )
        gravity_feet = Arrow(
            start=feet_pos + RIGHT * 1.0,
            end=feet_pos + RIGHT * 1.0 + DOWN * 1.5,
            color=ORANGE,
            stroke_width=7,
            buff=0,
        )

        self.play(
            GrowArrow(gravity_head),
            GrowArrow(gravity_feet),
            run_time=0.6,
        )
        self.wait(0.5)

        # 潮汐力矢印（両方下向き、長さが異なる）
        # Tidal force arrows (both pointing down, different lengths)
        tidal_head = Arrow(
            start=head_pos + RIGHT * 0.8,
            end=head_pos + RIGHT * 0.8 + DOWN * 0.6,
            color=RED,
            stroke_width=5,
            buff=0,
        )
        tidal_feet = Arrow(
            start=feet_pos + RIGHT * 0.8 + UP * 0.3,
            end=feet_pos + RIGHT * 0.8 + UP * 0.3 + DOWN * 1.0,
            color=RED,
            stroke_width=7,
            buff=0,
        )
        # 斜め下向きの圧縮矢印（地球中心方向）
        # Diagonal compression arrows (toward Earth's center)
        compress_left = Arrow(
            start=avatar.get_left() + LEFT * 0.5 + UP * 0.2,
            end=avatar.get_left() + RIGHT * 0.1 + DOWN * 0.4,
            color=BLUE,
            stroke_width=5,
            buff=0,
        )
        compress_right = Arrow(
            start=avatar.get_right() + RIGHT * 0.5 + UP * 0.2,
            end=avatar.get_right() + LEFT * 0.1 + DOWN * 0.4,
            color=BLUE,
            stroke_width=5,
            buff=0,
        )

        self.play(
            ReplacementTransform(gravity_head, tidal_head),
            ReplacementTransform(gravity_feet, tidal_feet),
            GrowArrow(compress_left),
            GrowArrow(compress_right),
            run_time=0.6,
        )

        # 引き伸ばし＆圧縮
        self.play(
            avatar.animate.stretch(1.12, dim=1).stretch(0.90, dim=0),
            tidal_head.animate.shift(DOWN * 0.15),
            tidal_feet.animate.shift(DOWN * 0.25),
            compress_left.animate.shift(RIGHT * 0.1 + DOWN * 0.1),
            compress_right.animate.shift(LEFT * 0.1 + DOWN * 0.1),
            run_time=0.8,
        )

        # 潮汐力ラベル（バックプレート付き）
        tidal_text = create_text_with_backplate(
            "潮汐力 / Tidal Force",
            font_size=32,
            text_color=YELLOW,
            bg_opacity=0.85,
        )
        tidal_text.move_to(RIGHT * 2.5 + DOWN * 2.5)

        self.play(FadeIn(tidal_text), run_time=0.6)
        self.wait(1.5)


if __name__ == "__main__":
    # コマンドラインから実行する場合のヘルプ
    print("使用方法:")
    print("  manim -pql scripts/tidal_stretch_body.py TidalStretchBody")
    print("  manim -pql scripts/tidal_stretch_body.py TidalStretchBodySimple")
    print("")
    print("シーン説明:")
    print("  TidalStretchBody       - 詳細版（段階的に説明、ラベル付き）")
    print("  TidalStretchBodySimple - シンプル版（短縮バージョン）")
    print("")
    print("脚本L11-15に対応:")
    print("  「重力による時空の曲がりの効果は、あなたの体にも起きています。」")
    print("  「足の方が地球に近いので、ほんの少しだけ強い重力を受けて、」")
    print("  「その結果、あなたの体は縦に少し引き伸ばされているんです。」")
