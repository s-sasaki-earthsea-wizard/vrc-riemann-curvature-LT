"""
月による潮汐力と海面変形のアニメーション（L88-89用）
Animation: Lunar tidal force and ocean deformation (for L88-89)

地球が受ける月の重力は、月に近い側と遠い側で強さが違う。
その差が、海水を引っ張って潮の満ち引きを起こしている。

The Moon's gravity on Earth differs between the near side and far side.
This difference pulls the ocean water, causing tides.
"""

from manim import *
import numpy as np


class OceanTides(Scene):
    """
    月による潮汐力で海面が変形するアニメーション（約13秒）
    Animation: Ocean deformation due to lunar tidal force (~13 seconds)
    """

    def construct(self):
        # 地球を作成
        # Create Earth
        earth_radius = 1.2
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.6)
        earth.set_stroke(color=BLUE_B, width=3)

        # 海水（最初は地球と同じ円形）
        # Ocean (initially circular like Earth)
        ocean = Circle(radius=earth_radius + 0.15, color=BLUE_A, fill_opacity=0.3)
        ocean.set_stroke(color=BLUE_A, width=2)

        # 地球グループ
        earth_group = VGroup(ocean, earth)
        earth_group.move_to(ORIGIN)

        # 月を作成（右側に配置）
        # Create Moon (positioned on the right)
        moon_distance = 3.5
        moon_radius = 0.35
        moon = Circle(radius=moon_radius, color=GRAY_B, fill_opacity=0.8)
        moon.set_stroke(color=WHITE, width=2)
        moon.move_to(RIGHT * moon_distance)

        # 月のラベル
        moon_label = Text("月", font_size=18, color=WHITE)
        moon_label_en = Text("Moon", font_size=12, color=GRAY)
        moon_labels = VGroup(moon_label, moon_label_en).arrange(DOWN, buff=0.05)
        moon_labels.next_to(moon, UP, buff=0.15)

        # 地球のラベル
        earth_label = Text("地球", font_size=18, color=BLUE_B)
        earth_label_en = Text("Earth", font_size=12, color=BLUE_A)
        earth_labels = VGroup(earth_label, earth_label_en).arrange(DOWN, buff=0.05)
        earth_labels.next_to(earth, DOWN, buff=0.3)

        # 表示
        self.play(
            GrowFromCenter(earth),
            GrowFromCenter(ocean),
            FadeIn(earth_labels),
            run_time=0.8,
        )
        self.play(
            GrowFromCenter(moon),
            FadeIn(moon_labels),
            run_time=0.6,
        )
        self.wait(0.3)

        # 重力矢印を表示（月に近い側は長く、遠い側は短く）
        # Show gravity arrows (longer on near side, shorter on far side)
        # 月に近い側（右側）
        arrow_near = Arrow(
            earth.get_right() + RIGHT * 0.1,
            earth.get_right() + RIGHT * 1.0,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        label_near = Text("強い", font_size=14, color=YELLOW)
        label_near_en = Text("Strong", font_size=10, color=YELLOW_A)
        label_near_group = VGroup(label_near, label_near_en).arrange(DOWN, buff=0.03)
        label_near_group.next_to(arrow_near, UP, buff=0.1)

        # 月から遠い側（左側）
        arrow_far = Arrow(
            earth.get_left() + LEFT * 0.1,
            earth.get_left() + RIGHT * 0.3,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.35,
        )
        label_far = Text("弱い", font_size=14, color=ORANGE)
        label_far_en = Text("Weak", font_size=10, color=ORANGE)
        label_far_group = VGroup(label_far, label_far_en).arrange(DOWN, buff=0.03)
        label_far_group.next_to(arrow_far, UP, buff=0.1)

        # 説明テキスト
        text1 = Text("月の重力は場所によって違う", font_size=22)
        text1_en = Text("Moon's gravity varies by location", font_size=16, color=GRAY)
        text1_group = VGroup(text1, text1_en).arrange(DOWN, buff=0.1)
        text1_group.to_edge(UP, buff=0.4)

        self.play(
            Write(text1_group),
            GrowArrow(arrow_near),
            GrowArrow(arrow_far),
            FadeIn(label_near_group),
            FadeIn(label_far_group),
            run_time=1.0,
        )
        self.wait(1.5)

        # 矢印とラベルをフェードアウト
        self.play(
            FadeOut(arrow_near),
            FadeOut(arrow_far),
            FadeOut(label_near_group),
            FadeOut(label_far_group),
            run_time=0.5,
        )

        # 海水が楕円形に変形
        # Ocean deforms into ellipse
        text2 = Text("その差が海水を引っ張る", font_size=22, color=YELLOW)
        text2_en = Text("This difference pulls the ocean", font_size=16, color=YELLOW_A)
        text2_group = VGroup(text2, text2_en).arrange(DOWN, buff=0.1)
        text2_group.to_edge(UP, buff=0.4)

        self.play(Transform(text1_group, text2_group))

        # 楕円形の海水（月に近い側と遠い側が膨らむ）
        # Elliptical ocean (bulges toward and away from Moon)
        ocean_deformed = Ellipse(
            width=(earth_radius + 0.15) * 2 + 0.8,  # 横に伸びる
            height=(earth_radius + 0.15) * 2 - 0.25,  # 縦に縮む
            color=BLUE_A,
            fill_opacity=0.3,
        )
        ocean_deformed.set_stroke(color=BLUE_A, width=2)

        # 変形の矢印（潮汐力の方向）
        bulge_arrow_right = Arrow(
            earth.get_right() + RIGHT * 0.2,
            earth.get_right() + RIGHT * 0.7,
            color=YELLOW,
            stroke_width=3,
        )
        bulge_arrow_left = Arrow(
            earth.get_left() + LEFT * 0.2,
            earth.get_left() + LEFT * 0.7,
            color=YELLOW,
            stroke_width=3,
        )

        self.play(
            Transform(ocean, ocean_deformed),
            GrowArrow(bulge_arrow_right),
            GrowArrow(bulge_arrow_left),
            run_time=1.5,
        )
        self.wait(0.5)

        # 矢印をフェードアウト
        self.play(
            FadeOut(bulge_arrow_right),
            FadeOut(bulge_arrow_left),
            run_time=0.3,
        )

        # 満潮・干潮のラベル
        # High tide / Low tide labels
        high_tide_right = Text("満潮", font_size=14, color=BLUE_B)
        high_tide_right.next_to(ocean, RIGHT, buff=0.1)

        high_tide_left = Text("満潮", font_size=14, color=BLUE_B)
        high_tide_left.next_to(ocean, LEFT, buff=0.1)

        low_tide_top = Text("干潮", font_size=14, color=BLUE_D)
        low_tide_top.next_to(ocean, UP, buff=0.1).shift(DOWN * 0.3)

        low_tide_bottom = Text("干潮", font_size=14, color=BLUE_D)
        low_tide_bottom.next_to(ocean, DOWN, buff=0.1).shift(UP * 0.3)

        self.play(
            FadeIn(high_tide_right),
            FadeIn(high_tide_left),
            FadeIn(low_tide_top),
            FadeIn(low_tide_bottom),
            run_time=0.6,
        )
        self.wait(0.5)

        # 結論テキスト
        text3 = Text("これが潮の満ち引き", font_size=26, color=YELLOW)
        text3_en = Text("This is the ocean tides", font_size=18, color=YELLOW_A)
        text3_group = VGroup(text3, text3_en).arrange(DOWN, buff=0.1)
        text3_group.to_edge(UP, buff=0.4)

        self.play(Transform(text1_group, text3_group))
        self.wait(0.5)

        # テロップ
        caption = Text("だから「潮汐」力", font_size=28, color=YELLOW)
        caption_en = Text("That's why 'Tidal' Force", font_size=20, color=YELLOW_A)
        caption_group = VGroup(caption, caption_en).arrange(DOWN, buff=0.1)
        caption_group.to_edge(DOWN, buff=0.5)

        box = SurroundingRectangle(caption_group, color=YELLOW, buff=0.2, corner_radius=0.1)

        self.play(
            Write(caption_group),
            Create(box),
            run_time=0.8,
        )
        self.wait(2)


class OceanTidesRotating(Scene):
    """
    月の公転に合わせて海面が変化するアニメーション
    Animation: Ocean surface changes as the Moon orbits
    """

    def construct(self):
        # 地球を作成
        # Create Earth
        earth_radius = 1.0
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.6)
        earth.set_stroke(color=BLUE_B, width=3)

        # 地球のラベル
        earth_label = Text("地球", font_size=16, color=BLUE_B)
        earth_label_en = Text("Earth", font_size=11, color=BLUE_A)
        earth_labels = VGroup(earth_label, earth_label_en).arrange(DOWN, buff=0.03)
        earth_labels.move_to(earth.get_center())

        # 海水（楕円形 - 潮汐変形）
        # Ocean (elliptical - tidal deformation)
        ocean_width = (earth_radius + 0.12) * 2 + 0.5
        ocean_height = (earth_radius + 0.12) * 2 - 0.15
        ocean = Ellipse(
            width=ocean_width,
            height=ocean_height,
            color=BLUE_A,
            fill_opacity=0.3,
        )
        ocean.set_stroke(color=BLUE_A, width=2)

        # 月の軌道
        # Moon's orbit
        orbit_radius = 2.8
        orbit = Circle(radius=orbit_radius, color=GRAY, stroke_width=1)
        orbit.set_stroke(opacity=0.3)

        # 月を作成
        # Create Moon
        moon_radius = 0.25
        moon = Circle(radius=moon_radius, color=GRAY_B, fill_opacity=0.8)
        moon.set_stroke(color=WHITE, width=2)
        moon.move_to(RIGHT * orbit_radius)

        # 月のラベル
        moon_label = Text("月", font_size=14, color=WHITE)
        moon_label.next_to(moon, UP, buff=0.1)

        # タイトル
        title = Text("月の公転と潮汐", font_size=24)
        title_en = Text("Lunar Orbit and Tides", font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)

        # 初期表示
        self.play(
            Write(title_group),
            Create(orbit),
            GrowFromCenter(earth),
            GrowFromCenter(ocean),
            FadeIn(earth_labels),
            run_time=1.0,
        )
        self.play(
            GrowFromCenter(moon),
            FadeIn(moon_label),
            run_time=0.5,
        )
        self.wait(0.5)

        # 月と海水の回転アニメーション
        # Rotation animation for Moon and ocean
        # 月は軌道上を回り、海水（楕円）は月の方向に合わせて回転

        # 回転のトラッカー
        angle_tracker = ValueTracker(0)

        # 月の位置を更新する関数
        def update_moon(m):
            angle = angle_tracker.get_value()
            m.move_to(
                np.array(
                    [
                        orbit_radius * np.cos(angle),
                        orbit_radius * np.sin(angle),
                        0,
                    ]
                )
            )

        # 月のラベル位置を更新
        def update_moon_label(label):
            label.next_to(moon, UP, buff=0.1)

        # 海水の回転を更新
        def update_ocean(o):
            angle = angle_tracker.get_value()
            new_ocean = Ellipse(
                width=ocean_width,
                height=ocean_height,
                color=BLUE_A,
                fill_opacity=0.3,
            )
            new_ocean.set_stroke(color=BLUE_A, width=2)
            new_ocean.rotate(angle)
            o.become(new_ocean)

        moon.add_updater(update_moon)
        moon_label.add_updater(update_moon_label)
        ocean.add_updater(update_ocean)

        # 説明テキスト
        explain = Text("海面は常に月の方向に膨らむ", font_size=20, color=YELLOW)
        explain_en = Text(
            "Ocean always bulges toward the Moon", font_size=14, color=YELLOW_A
        )
        explain_group = VGroup(explain, explain_en).arrange(DOWN, buff=0.1)
        explain_group.to_edge(DOWN, buff=0.4)

        self.play(Write(explain_group), run_time=0.5)

        # 1周回転（約8秒）
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=rate_functions.linear,
        )

        # アップデーターを削除
        moon.remove_updater(update_moon)
        moon_label.remove_updater(update_moon_label)
        ocean.remove_updater(update_ocean)

        # 結論
        conclusion = Text("だから「潮汐」力", font_size=26, color=YELLOW)
        conclusion_en = Text("That's why 'Tidal' Force", font_size=18, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.4)

        self.play(Transform(explain_group, conclusion_group))
        self.wait(2)


class OceanTidesCombined(Scene):
    """
    潮汐力の説明 + 月の公転アニメーション（組み合わせ版、約13秒）
    Combined: Tidal force explanation + lunar orbit animation (~13 seconds)
    """

    def construct(self):
        # パート1: 静的な説明（短縮版）
        # Part 1: Static explanation (shortened)

        # 地球を作成
        earth_radius = 1.0
        earth = Circle(radius=earth_radius, color=BLUE, fill_opacity=0.6)
        earth.set_stroke(color=BLUE_B, width=3)

        # 海水（最初は円形）
        ocean = Circle(radius=earth_radius + 0.12, color=BLUE_A, fill_opacity=0.3)
        ocean.set_stroke(color=BLUE_A, width=2)

        # 月
        moon_distance = 3.0
        moon_radius = 0.28
        moon = Circle(radius=moon_radius, color=GRAY_B, fill_opacity=0.8)
        moon.set_stroke(color=WHITE, width=2)
        moon.move_to(RIGHT * moon_distance)

        # ラベル
        moon_label = Text("月", font_size=14, color=WHITE)
        moon_label.next_to(moon, UP, buff=0.1)

        earth_label = Text("地球", font_size=14, color=BLUE_B)
        earth_label.move_to(earth.get_center())

        # 表示
        self.play(
            GrowFromCenter(earth),
            GrowFromCenter(ocean),
            FadeIn(earth_label),
            GrowFromCenter(moon),
            FadeIn(moon_label),
            run_time=0.8,
        )

        # 重力矢印
        arrow_near = Arrow(
            earth.get_right() + RIGHT * 0.1,
            earth.get_right() + RIGHT * 0.8,
            color=YELLOW,
            stroke_width=3,
        )
        arrow_far = Arrow(
            earth.get_left() + LEFT * 0.1,
            earth.get_left() + RIGHT * 0.25,
            color=ORANGE,
            stroke_width=2,
        )

        text1 = Text("月の重力は場所によって違う", font_size=20)
        text1_en = Text("Moon's gravity varies by location", font_size=14, color=GRAY)
        text1_group = VGroup(text1, text1_en).arrange(DOWN, buff=0.1)
        text1_group.to_edge(UP, buff=0.3)

        self.play(
            Write(text1_group),
            GrowArrow(arrow_near),
            GrowArrow(arrow_far),
            run_time=0.8,
        )
        self.wait(1)

        # 海水が楕円に変形
        self.play(FadeOut(arrow_near), FadeOut(arrow_far), run_time=0.3)

        ocean_width = (earth_radius + 0.12) * 2 + 0.5
        ocean_height = (earth_radius + 0.12) * 2 - 0.15
        ocean_deformed = Ellipse(
            width=ocean_width,
            height=ocean_height,
            color=BLUE_A,
            fill_opacity=0.3,
        )
        ocean_deformed.set_stroke(color=BLUE_A, width=2)

        text2 = Text("海水が引っ張られる", font_size=20, color=YELLOW)
        text2_en = Text("Ocean water is pulled", font_size=14, color=YELLOW_A)
        text2_group = VGroup(text2, text2_en).arrange(DOWN, buff=0.1)
        text2_group.to_edge(UP, buff=0.3)

        self.play(
            Transform(text1_group, text2_group),
            Transform(ocean, ocean_deformed),
            run_time=1.0,
        )
        self.wait(0.5)

        # パート2: 月の公転
        # Part 2: Lunar orbit

        # 軌道を追加
        orbit_radius = moon_distance
        orbit = Circle(radius=orbit_radius, color=GRAY, stroke_width=1)
        orbit.set_stroke(opacity=0.3)

        text3 = Text("月が回ると潮汐も回る", font_size=20, color=YELLOW)
        text3_en = Text("As Moon orbits, tides follow", font_size=14, color=YELLOW_A)
        text3_group = VGroup(text3, text3_en).arrange(DOWN, buff=0.1)
        text3_group.to_edge(UP, buff=0.3)

        self.play(
            Transform(text1_group, text3_group),
            Create(orbit),
            run_time=0.5,
        )

        # 回転アニメーション
        angle_tracker = ValueTracker(0)

        def update_moon(m):
            angle = angle_tracker.get_value()
            m.move_to(
                np.array(
                    [
                        orbit_radius * np.cos(angle),
                        orbit_radius * np.sin(angle),
                        0,
                    ]
                )
            )

        def update_moon_label(label):
            label.next_to(moon, UP, buff=0.1)

        def update_ocean(o):
            angle = angle_tracker.get_value()
            new_ocean = Ellipse(
                width=ocean_width,
                height=ocean_height,
                color=BLUE_A,
                fill_opacity=0.3,
            )
            new_ocean.set_stroke(color=BLUE_A, width=2)
            new_ocean.rotate(angle)
            o.become(new_ocean)

        moon.add_updater(update_moon)
        moon_label.add_updater(update_moon_label)
        ocean.add_updater(update_ocean)

        # 1周回転（約6秒）
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=6,
            rate_func=rate_functions.linear,
        )

        moon.remove_updater(update_moon)
        moon_label.remove_updater(update_moon_label)
        ocean.remove_updater(update_ocean)

        # 結論
        conclusion = Text("だから「潮汐」力", font_size=24, color=YELLOW)
        conclusion_en = Text("That's why 'Tidal' Force", font_size=16, color=YELLOW_A)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.1)
        conclusion_group.to_edge(DOWN, buff=0.4)

        box = SurroundingRectangle(
            conclusion_group, color=YELLOW, buff=0.15, corner_radius=0.1
        )

        self.play(Write(conclusion_group), Create(box), run_time=0.6)
        self.wait(1.5)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/ocean_tides.py OceanTides")
    print("  manim -pql scripts/ocean_tides.py OceanTidesRotating")
    print("  manim -pql scripts/ocean_tides.py OceanTidesCombined")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  OceanTides         - 静的な潮汐力の説明（約13秒）")
    print("                       Static tidal force explanation (~13s)")
    print("  OceanTidesRotating - 月の公転に合わせて海面が変化（約12秒）")
    print("                       Ocean changes as Moon orbits (~12s)")
    print("  OceanTidesCombined - 説明 + 公転の組み合わせ（約13秒、推奨）")
    print("                       Explanation + orbit combined (~13s, recommended)")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
