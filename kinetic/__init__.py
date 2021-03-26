def velocity_refresh(A, V, dt):
    v_x, v_y = V[0], V[1]
    v_y = v_y + A * dt
    V = [v_x, v_y]
    return V


def position_refresh(S, V, A, dt):
    S_x, S_y = S[0], S[1]
    S_x = S_x + V[0] * dt
    S_y = S_y + V[1] * dt + (A * dt ** 2) / 2
    S = [S_x, S_y]
    return S
