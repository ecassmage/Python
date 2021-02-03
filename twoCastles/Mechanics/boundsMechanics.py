class Bounds:
    def __init__(self, corners):
        """So as to hopefully raise error if not enough coordinates were given. Don't want to write my own exception"""
        w, x, y, z = corners
        self.corners = (w, x, y, z)


def bounds(shape_obj, coord):
    w, x, y, z = shape_obj.corners
    ref_x, ref_y = coord
    if w <= ref_x <= y and x <= ref_y <= z:
        return True
