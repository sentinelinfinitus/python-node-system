from kivy.lang import Builder
from kivy.app import App

KV = '''
<Node@Scatter>:
    # do_scale: False
    # do_rotation: False
    size_hint: None, None
    size: 200, 100
    color: [0, 0, 0, 1]
    canvas.before:
        Color:
            rgba: root.color
        RoundedRectangle:
            pos: 0, 0
            size: self.size
            radius: 10, 10
FloatLayout:
    pos_one: one.pos
    pos_two: two.pos
    canvas.before:
        Line:
            width: 2
            bezier:
                (app.generate_bezier(self.ids.one, self.ids.two)
                if (
                'one' in self.ids and 'two' in self.ids
                and self.pos_one and self.pos_two
                ) else [])
    Node:
        id: one
        color: [.5, .5, 0, 1]
    Node:
        id: two
        color: [0, .5, .0, 1]
'''

class Nodes(App):
    def build(self):
        return Builder.load_string(KV)

    def generate_bezier(self, a, b):
        xd, yd = abs(a.x - b.x), abs(a.y - b.y)
        if xd > yd:
            key = 0
            offset = xd / 5
        else:
            key = 1
            offset = yd / 5

        a, b = sorted([a, b], key=lambda a: a.pos[key])

        if key == 0:
            return [
                a.right, a.center_y,
                a.right + offset, a.center_y,
                b.x - offset, b.center_y,
                b.x, b.center_y
            ]
        else:
            return [
                a.center_x, a.top,
                a.center_x, a.top + offset,
                b.center_x, b.y - offset,
                b.center_x, b.y
            ]

if __name__ == '__main__':
    try:
        Nodes().run()
    except:
        import pdb; pdb.post_mortem();
        raise