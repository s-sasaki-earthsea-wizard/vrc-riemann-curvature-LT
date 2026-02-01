"""
球面上での平行移動
Parallel Transport on a Sphere

北極点から出発し、赤道へ下り、赤道上を90度移動し、再び北極点に戻る。
このとき、ベクトルの向きが90度ずれることを示すアニメーション。

Starting from the North Pole, moving to the equator, traveling 90 degrees
along the equator, and returning to the North Pole. This animation shows
that the vector's direction shifts by 90 degrees.

yt_script.md L160-169 の解説用
目標時間: 35-40秒
"""

from manim import *
import numpy as np


class ParallelTransportSphere(ThreeDScene):
    """
    球面上での平行移動アニメーション
    Parallel transport animation on a sphere

    曲がった空間（球面）では、方向を保ったまま一周しても
    元の向きに戻らないことを示す。

    Shows that on a curved space (sphere), even if you maintain
    your direction throughout a loop, you don't return to
    the original orientation.
    """

    def construct(self):
        # ===== カメラ設定（斜め上から固定） =====
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # ===== タイトル（2D オーバーレイ） =====
        # 3Dシーンでは固定テキストを追加
        title = Text("球面上での平行移動", font_size=28)
        title_en = Text("Parallel Transport on a Sphere", font_size=16, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(title_group)

        self.play(Write(title_group), run_time=1.0)
        self.wait(0.5)

        # ===== 球を作成 =====
        sphere_radius = 2.0
        sphere = Sphere(
            radius=sphere_radius,
            resolution=(32, 32),
            fill_opacity=1.0,  # 不透明
            stroke_width=0,
        )
        sphere.set_color(BLUE_E)

        self.play(Create(sphere), run_time=1.5)
        self.wait(0.3)

        # ===== 北極点マーカー =====
        north_pole_pos = sphere_radius * UP

        # ===== 経路を定義 =====
        # 経路1: 北極 → 赤道（経度0度の経線に沿って）
        # 経路2: 赤道上を90度東へ（経度0度 → 経度90度）
        # 経路3: 赤道 → 北極（経度90度の経線に沿って）

        # 球面座標での経路点を計算
        def spherical_to_cartesian(theta, phi, r=sphere_radius):
            """球面座標 (theta: 天頂角, phi: 方位角) → デカルト座標"""
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            return np.array([x, y, z])

        # 経路の点を生成
        # 経路を45度時計回りに回転させて、全体が前面に見えるようにする
        num_points = 30
        phi_start = -PI / 2  # -90度（手前左端）
        phi_end = 0          # 0度（手前中央）

        # 経路1: 北極(theta=0) → 赤道(theta=PI/2)、phi=-45度
        path1_points = [
            spherical_to_cartesian(t * PI / 2, phi_start)
            for t in np.linspace(0, 1, num_points)
        ]

        # 経路2: 赤道上、phi=-45度 → phi=+45度（90度分）
        path2_points = [
            spherical_to_cartesian(PI / 2, phi_start + t * PI / 2)
            for t in np.linspace(0, 1, num_points)
        ]

        # 経路3: 赤道(theta=PI/2) → 北極(theta=0)、phi=+45度
        path3_points = [
            spherical_to_cartesian((1 - t) * PI / 2, phi_end)
            for t in np.linspace(0, 1, num_points)
        ]

        # 経路を曲線として作成（目立つように太く明るい色）
        def create_path_curve(points, color, opacity=0.5, width=4):
            curve = VMobject(color=color, stroke_width=width, stroke_opacity=opacity)
            curve.set_points_smoothly(points)
            return curve

        # プレビュー用（薄め）
        preview_path1 = create_path_curve(path1_points, YELLOW, 0.4, 3)
        preview_path2 = create_path_curve(path2_points, YELLOW, 0.4, 3)
        preview_path3 = create_path_curve(path3_points, YELLOW, 0.4, 3)

        # 経路プレビューを表示
        path_preview_text = Text("三角形の経路を移動", font_size=16, color=WHITE)
        path_preview_text_en = Text("Moving along a triangular path", font_size=12, color=GRAY)
        path_preview_group = VGroup(path_preview_text, path_preview_text_en).arrange(DOWN, buff=0.05)
        path_preview_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(path_preview_group)

        self.play(
            Create(preview_path1),
            Create(preview_path2),
            Create(preview_path3),
            Write(path_preview_group),
            run_time=1.2,
        )
        self.wait(0.5)

        # ===== ベクトルを配置（北極点） =====
        # 初期方向は「南」= 経路1の方向（phi_start方向）
        vector_length = 0.6
        phi_vec_initial = phi_start  # -90度（Y軸負方向、カメラから見て左）

        # 初期ベクトル方向
        initial_direction = np.array([np.cos(phi_vec_initial), np.sin(phi_vec_initial), 0])

        def create_tangent_vector(position, direction, color=RED):
            """球面上の接ベクトルを作成"""
            arrow = Arrow3D(
                start=position,
                end=position + direction * vector_length,
                color=color,
                thickness=0.02,
                height=0.15,
                base_radius=0.06,
            )
            return arrow

        # 北極点にベクトルを配置
        vector = create_tangent_vector(north_pole_pos, initial_direction)

        # ===== ステップ1: 北極 → 赤道 =====
        step1_text = Text("①北極から赤道へ", font_size=16, color=RED_A)
        step1_text_en = Text("Step 1: North Pole to Equator", font_size=12, color=RED_A)
        step1_group = VGroup(step1_text, step1_text_en).arrange(DOWN, buff=0.05)
        step1_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(step1_group)

        # 軌跡用の曲線（太く明るく）
        trace_path1 = create_path_curve(path1_points, YELLOW, 1.0, 5)

        self.play(FadeOut(path_preview_group), run_time=0.3)
        self.play(FadeIn(step1_group), run_time=0.3)

        # ベクトルを経路に沿って移動（平行移動）
        # 北極→赤道では、ベクトルは常に「南」を向く
        # しかし球面上では、これは経線に沿った方向を維持すること
        # 赤道に着いたとき、ベクトルは赤道に平行（東西方向ではなく経線方向）

        move_duration = 4.0

        # 経路1のアニメーション
        def update_vector_path1(mob, alpha):
            """経路1でのベクトル更新（北極→赤道）"""
            theta = alpha * PI / 2  # 0 → PI/2
            phi = phi_start  # -45度
            pos = spherical_to_cartesian(theta, phi)

            # 平行移動: 経線に沿って移動するとき
            # 初期方向（-90度）を維持しながら、球面の接平面に沿って変化
            # 赤道に着いたとき、ベクトルは真下（-Z）を向く
            # 補間: 北極で[-90度方向]、赤道で[-Z方向]
            t = alpha
            direction = np.array([
                (1 - t) * np.cos(phi_vec_initial),
                (1 - t) * np.sin(phi_vec_initial),
                -t,
            ])
            norm = np.linalg.norm(direction)
            if norm > 0.01:
                direction = direction / norm

            mob.become(create_tangent_vector(pos, direction))

        self.play(
            UpdateFromAlphaFunc(vector, update_vector_path1),
            Create(trace_path1),
            run_time=move_duration,
            rate_func=linear,
        )
        self.wait(0.3)

        # ===== ステップ2: 赤道上を90度東へ =====
        step2_text = Text("②赤道に沿って90度", font_size=16, color=GREEN_A)
        step2_text_en = Text("Step 2: 90° along Equator", font_size=12, color=GREEN_A)
        step2_group = VGroup(step2_text, step2_text_en).arrange(DOWN, buff=0.05)
        step2_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(step2_group)

        trace_path2 = create_path_curve(path2_points, YELLOW, 1.0, 5)

        self.play(FadeOut(step1_group), run_time=0.3)
        self.play(FadeIn(step2_group), run_time=0.3)

        def update_vector_path2(mob, alpha):
            """経路2でのベクトル更新（赤道上を東へ）"""
            theta = PI / 2  # 赤道上
            phi = phi_start + alpha * PI / 2  # -45度 → +45度

            pos = spherical_to_cartesian(theta, phi)

            # 平行移動: 赤道に沿って移動するとき
            # 赤道上では南向き = 真下（-Z方向）
            direction = np.array([0, 0, -1])

            mob.become(create_tangent_vector(pos, direction))

        self.play(
            UpdateFromAlphaFunc(vector, update_vector_path2),
            Create(trace_path2),
            run_time=move_duration,
            rate_func=linear,
        )
        self.wait(0.3)

        # ===== ステップ3: 赤道 → 北極 =====
        step3_text = Text("③北極へ戻る", font_size=16, color=ORANGE)
        step3_text_en = Text("Step 3: Return to North Pole", font_size=12, color=ORANGE)
        step3_group = VGroup(step3_text, step3_text_en).arrange(DOWN, buff=0.05)
        step3_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(step3_group)

        trace_path3 = create_path_curve(path3_points, YELLOW, 1.0, 5)

        self.play(FadeOut(step2_group), run_time=0.3)
        self.play(FadeIn(step3_group), run_time=0.3)

        # 経路3の最終位置を事前に計算（ゴーストベクトルでも使用）
        final_pos = spherical_to_cartesian(0, phi_end)  # 北極点（theta=0）
        final_normal = final_pos / np.linalg.norm(final_pos)
        final_offset_pos = final_pos + final_normal * 0.05

        def update_vector_path3(mob, alpha):
            """経路3でのベクトル更新（赤道→北極）"""
            theta = (1 - alpha) * PI / 2  # PI/2 → 0
            phi = phi_end  # 0度

            pos = spherical_to_cartesian(theta, phi)

            # ベクトルを球面から少し浮かせて、経路より前面に表示
            # 法線方向（球の中心から外向き）にオフセット
            normal = pos / np.linalg.norm(pos)
            offset_pos = pos + normal * 0.05  # 0.05だけ浮かせる

            # 平行移動: 経線に沿って北へ戻るとき
            # 赤道で下向き（-Z）だったベクトルは、
            # 北極に着いたとき、初期方向から90度ずれた方向を向く
            # 初期: -90度 → 最終: 0度（X軸正方向）

            # 補間: 赤道で[0,0,-1]、北極で[phi_end方向]
            t = alpha
            phi_vec_final = phi_end  # 0度（X軸正方向、90度ずれ）
            final_dir = np.array([np.cos(phi_vec_final), np.sin(phi_vec_final), 0])
            direction = np.array([
                t * final_dir[0],
                t * final_dir[1],
                -(1 - t),
            ])
            norm = np.linalg.norm(direction)
            if norm > 0.01:
                direction = direction / norm
            else:
                direction = final_dir

            mob.become(create_tangent_vector(offset_pos, direction))

        # ベクトルと経路を同時にアニメーション
        self.play(
            UpdateFromAlphaFunc(vector, update_vector_path3),
            Create(trace_path3),
            run_time=move_duration,
            rate_func=linear,
        )
        self.wait(0.5)

        # ===== 結果の強調 =====
        # 初期方向のゴーストベクトルを、経路3の最終位置と同じ位置から表示
        # 直交する2つのベクトルが並んで見える
        ghost_vector = Arrow3D(
            start=final_offset_pos,
            end=final_offset_pos + initial_direction * vector_length,
            color=RED,
            thickness=0.015,
            height=0.12,
            base_radius=0.05,
        )
        ghost_vector.set_opacity(0.4)

        self.play(FadeIn(ghost_vector), run_time=0.5)
        self.wait(0.3)

        # ===== 結論 =====
        self.play(FadeOut(step3_group), run_time=0.3)

        conclusion_text = Text("曲がった空間では向きが変わる", font_size=20, color=WHITE)
        conclusion_text_en = Text("Direction changes in curved space", font_size=14, color=GRAY)
        conclusion_group = VGroup(conclusion_text, conclusion_text_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(conclusion_group)

        self.play(FadeIn(conclusion_group), run_time=0.5)
        self.wait(0.5)

        # 90度ずれたことを強調
        angle_text = Text("90°回転", font_size=24, color=YELLOW)
        angle_text_en = Text("90° rotation", font_size=14, color=YELLOW_A)
        angle_group = VGroup(angle_text, angle_text_en).arrange(DOWN, buff=0.05)
        angle_group.next_to(conclusion_group, UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(angle_group)

        self.play(FadeIn(angle_group), run_time=0.5)
        self.wait(2.0)

        # フェードアウト
        self.play(
            FadeOut(title_group),
            FadeOut(conclusion_group),
            FadeOut(angle_group),
            FadeOut(sphere),
            FadeOut(preview_path1),
            FadeOut(preview_path2),
            FadeOut(preview_path3),
            FadeOut(trace_path1),
            FadeOut(trace_path2),
            FadeOut(trace_path3),
            FadeOut(vector),
            FadeOut(ghost_vector),
            run_time=1.0,
        )


class ParallelTransportSphereSimple(ThreeDScene):
    """
    シンプル版：最小構成
    Simple version: Minimal configuration
    """

    def construct(self):
        # カメラ設定
        self.set_camera_orientation(phi=60 * DEGREES, theta=-50 * DEGREES)

        # 球
        sphere_radius = 2.0
        sphere = Sphere(radius=sphere_radius, resolution=(24, 24), fill_opacity=0.25)
        sphere.set_color(BLUE_E)

        # 赤道
        equator = Circle(radius=sphere_radius, color=YELLOW_A, stroke_width=2)
        equator.rotate(PI / 2, axis=RIGHT)

        self.add(sphere, equator)

        # 経路の計算
        def spherical_to_cartesian(theta, phi, r=sphere_radius):
            return np.array([
                r * np.sin(theta) * np.cos(phi),
                r * np.sin(theta) * np.sin(phi),
                r * np.cos(theta),
            ])

        # 経路点
        n = 20
        path1 = [spherical_to_cartesian(t * PI / 2, 0) for t in np.linspace(0, 1, n)]
        path2 = [spherical_to_cartesian(PI / 2, t * PI / 2) for t in np.linspace(0, 1, n)]
        path3 = [spherical_to_cartesian((1 - t) * PI / 2, PI / 2) for t in np.linspace(0, 1, n)]

        # 経路を表示
        for points, color in [(path1, RED), (path2, GREEN), (path3, ORANGE)]:
            curve = VMobject(color=color, stroke_width=2, stroke_opacity=0.5)
            curve.set_points_smoothly(points)
            self.add(curve)

        # ベクトル
        vector_length = 0.5
        north_pole = sphere_radius * UP

        vector = Arrow3D(
            start=north_pole,
            end=north_pole + RIGHT * vector_length,
            color=RED,
            thickness=0.015,
        )
        self.add(vector)

        self.wait(0.5)

        # 移動アニメーション（簡略版）
        def make_vector(pos, direction):
            return Arrow3D(
                start=pos,
                end=pos + direction * vector_length,
                color=RED,
                thickness=0.015,
            )

        # 経路1
        for i, t in enumerate(np.linspace(0, 1, 15)):
            theta = t * PI / 2
            pos = spherical_to_cartesian(theta, 0)
            direction = np.array([np.cos(theta), 0, -np.sin(theta)])
            new_vector = make_vector(pos, direction)
            self.play(Transform(vector, new_vector), run_time=0.15)

        # 経路2
        for t in np.linspace(0, 1, 15):
            phi = t * PI / 2
            pos = spherical_to_cartesian(PI / 2, phi)
            direction = np.array([0, 0, -1])
            new_vector = make_vector(pos, direction)
            self.play(Transform(vector, new_vector), run_time=0.15)

        # 経路3
        for t in np.linspace(0, 1, 15):
            theta = (1 - t) * PI / 2
            pos = spherical_to_cartesian(theta, PI / 2)
            interp = t
            direction = np.array([0, interp, -(1 - interp)])
            if np.linalg.norm(direction) > 0.01:
                direction = direction / np.linalg.norm(direction)
            new_vector = make_vector(pos, direction)
            self.play(Transform(vector, new_vector), run_time=0.15)

        self.wait(1)

        # 結果表示
        result = Text("90°ずれた！", font_size=20, color=YELLOW)
        result.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(result)
        self.play(Write(result))
        self.wait(2)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/parallel_transport_sphere.py ParallelTransportSphere")
    print("  manim -pql scripts/parallel_transport_sphere.py ParallelTransportSphereSimple")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  ParallelTransportSphere       - 基本版（詳細なアニメーション）")
    print("                                  Basic version (detailed animation)")
    print("  ParallelTransportSphereSimple - シンプル版（最小構成）")
    print("                                  Simple version (minimal)")
