from ltypes import ccall, f32, f64, i32, i64, CPtr, pointer, Pointer, p_c_pointer

@ccall
def f_i32_i32(x: i32) -> i32:
    pass

@ccall
def f_pi32_i32(x: CPtr) -> i32:
    pass

@ccall
def driver1() -> i32:
    pass

@ccall
def driver2() -> i32:
    pass

@ccall
def driver3() -> i32:
    pass

@ccallback
def callback1() -> i32:
    xi32: i32
    xi32 = 3
    p: CPtr
    p_c_pointer(pointer(xi32), p)
    return f_pi32_i32(p)

@ccallback
def callback2(x: i32) -> i32:
    return f_i32_i32(x)

@ccallback
def callback3(p: CPtr) -> i32:
    return f_pi32_i32(p)


def test_c_callbacks():
    assert driver1() == 4
    assert driver2() == 4
    assert driver3() == 4


test_c_callbacks()