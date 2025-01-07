"""
画N叉树,并且在边上添加数字标签
"""

from manim import *

class TreeDiagramWithLabels(Scene):
    def construct(self):
        # 定义节点内容
        nodes = {
            "A": "1 \\ 2 \\ 3 \\ 4",
            "B1": "2 \\ 3 \\ 4", 
            "B2": "3 \\ 4", 
            "B3": "4", 
            "B4": "None",
            "C1": "[1, \\ 2]", 
            "C2": "[1, \\ 3]", 
            "C3": "[1, \\ 4]", 
            "C4": "[2, \\ 3]", 
            "C5": "[2, \\ 4]", 
            "C6": "[3, \\ 4]"
        }

        # 定义节点位置
        positions = {
            "A": UP * 3,
            "B1": LEFT * 4 + UP * 1, 
            "B2": LEFT * 1 + UP * 1, 
            "B3": RIGHT * 1 + UP * 1, 
            "B4": RIGHT * 4 + UP * 1,
            "C1": LEFT * 5 + DOWN * 1, 
            "C2": LEFT * 4 + DOWN * 1, 
            "C3": LEFT * 3 + DOWN * 1, 
            "C4": LEFT * 1.5 + DOWN * 1, 
            "C5": LEFT * 0.5 + DOWN * 1, 
            "C6": RIGHT * 1 + DOWN * 1
        }

        # 定义边的标签（选择的数字）
        edge_labels = {
            ("A", "B1"): "1", 
            ("A", "B2"): "2", 
            ("A", "B3"): "3", 
            ("A", "B4"): "4",
            ("B1", "C1"): "2", 
            ("B1", "C2"): "3", 
            ("B1", "C3"): "4", 
            ("B2", "C4"): "3", 
            ("B2", "C5"): "4", 
            ("B3", "C6"): "4"
        }

        # 创建节点的字典，使用 MathTex 来确保一致的显示效果
        graph_nodes = {}
        for key, value in nodes.items():
            try:
                graph_nodes[key] = MathTex(value).scale(0.8)
            except Exception as e:
                print(f"Error with node {key}: {e}")

        # 将节点放置到对应位置
        for key, node in graph_nodes.items():
            node.move_to(positions[key])

        # 创建所有边
        edges = [
            ("A", "B1"), 
            ("A", "B2"), 
            ("A", "B3"), 
            ("A", "B4"),
            ("B1", "C1"), 
            ("B1", "C2"), 
            ("B1", "C3"), 
            ("B2", "C4"), 
            ("B2", "C5"), 
            ("B3", "C6")
        ]

        # 绘制节点
        self.play(*[FadeIn(node) for node in graph_nodes.values()])

        # 绘制边和标签
        for edge in edges:
            start = positions[edge[0]]
            end = positions[edge[1]]

            # 计算方向向量并归一化
            direction = end - start
            direction_unit = direction / np.linalg.norm(direction)

            # 定义线的起始和结束点，留出一定的距离
            line_start = start + 0.3 * direction_unit  # 从起始点向外移动
            line_end = end - 0.3 * direction_unit      # 从结束点向内移动

            # 绘制蓝色连线
            line = Line(line_start, line_end, color=BLUE)
            self.play(Create(line), run_time=0.5)

            # 添加边上的数字标签，设置为黄色
            mid_point = (line_start + line_end) / 2
            label = MathTex(edge_labels[edge]).scale(0.8).set_color(YELLOW).move_to(mid_point + DOWN * 0.2)
            self.play(FadeIn(label))

        # 显示最终图形
        self.wait(3)