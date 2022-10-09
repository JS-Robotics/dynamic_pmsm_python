from math import sin, cos, sqrt


def clarke_transform(a, b, c):
    """
    Transform from three-phase to alpha-beta reference
    :param a: Phase a value
    :param b: Phase b value
    :param c: Phase c value
    :return: alpha, beta
    """
    alpha = 2 / 3 * (a - 0.5 * b - 0.5 * c)
    beta = 2 / 3 * (sqrt(3) / 2 * b - sqrt(3) / 2 * c)
    return alpha, beta


def park_transform(alpha, beta, angle):
    """
    Transform from alpha-beta reference to synchronous dq-axis
    :param alpha: Phase alpha value
    :param beta:  Phase beta value
    :param angle: Electrical angular position
    :return: d, q
    """
    d = cos(angle) * alpha + sin(angle) * beta
    q = -sin(angle) * alpha + cos(angle) * beta
    return d, q


def inverse_clarke_transform(alpha, beta):
    a = alpha
    b = -0.5*alpha + sqrt(3)/2*beta
    c = -0.5*alpha - sqrt(3)/2*beta
    return a, b, c


def inverse_parke_transform(d, q, angle):
    alpha = cos(angle)*q - sin(angle)*d
    beta = sin(angle)*q + cos(angle)*d
    return alpha, beta
