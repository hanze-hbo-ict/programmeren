# Extra functies voor VPython voor het web

```python
def wall_collide(w, obj):
    """ w is a wall
        obj is a moving object
        returns True (and reflects obj.vel) if it collides...
          + ALSO: runs obj.pos = obj.pos - obj.vel*dt to "undo" the collision
        returns False (w/o changing obj) if there's no collision
        all y components are ignored throughout!
    """
    b = obj  # heeft nu de naam b, maar moet obj zijn!!
    wpos_noy = vector(w.pos)
    wpos_noy.y = 0.0
    waxis_noy = vector(w.axis)
    waxis_noy.y = 0.0
    waxis_norm = norm(waxis_noy)
    wperp_norm = rotate(waxis_norm, radians(90), vector(0, 1, 0))
    bpos_noy = vector(b.pos)
    bpos_noy.y = 0.0
    bdiff_noy = bpos_noy - wpos_noy
    bvel_noy = vector(b.vel)
    bvel_noy.y = 0.0
    b_axial = dot(waxis_norm, bdiff_noy)
    b_perp = dot(wperp_norm, bdiff_noy)
    b_vel_axial = dot(waxis_norm, bvel_noy)
    b_vel_perp = dot(wperp_norm, bvel_noy)
    
    w_length = abs(w.size.x)/2  # symmetrisch rond het midden
    w_height = abs(w.size.y)/2  # genegeerd
    w_depth = abs(w.size.z)/2   # symmetrisch rond het midden
    smallest_dim = max(0.1, min(w_length, w_depth))
    
    if mag(wpos_noy - bpos_noy) < smallest_dim or (-w_length < b_axial < w_length and -w_depth < b_perp < w_depth):
        # geraakt langs de as van w_length (axis) of...
        print("In rechthoek!")
        b.pos = b.pos - b.vel * dt  # laatste beweging ongedaan maken
        new_b_vel = b_vel_axial * waxis_norm - b_vel_perp*wperp_norm
        new_b_vel.y = b.vel.y   # de oude y-component van de snelheid herstellen...
        b.vel = new_b_vel
        return True
    else:
        return False
```