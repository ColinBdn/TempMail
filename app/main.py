import OpenGL.GL as gl
from imgui_bundle.python_backends.glfw_backend import GlfwRenderer
import glfw
from imgui_bundle import imgui, imgui_ctx
from imgui_bundle import imgui_md

import sys
import app

def init_fonts_and_markdown():
    # uncomment to keep using the default hardcoded font, or load your default font here
    # imgui.get_io().fonts.add_font_default()

    # Load markdown fonts
    imgui_md.initialize_markdown()
    font_loader = imgui_md.get_font_loader_function()
    font_loader()


def main():
    window = impl_glfw_init()
    imgui.create_context()
    impl = GlfwRenderer(window)

    imgui.get_io().config_flags |= imgui.ConfigFlags_.docking_enable

    
    init_fonts_and_markdown()

    app.init()

    while not glfw.window_should_close(window):
        glfw.wait_events()
        impl.process_inputs()
        imgui.new_frame()
        imgui.dock_space_over_viewport(flags=imgui.DockNodeFlags_.auto_hide_tab_bar)
        

        app.loop()

        gl.glClearColor(0.0, 0.0, 0.0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()


def impl_glfw_init():
    width, height = 1280, 720
    window_name = "Temp Mail"

    if not glfw.init():
        print("Could not initialize OpenGL context")
        sys.exit(1)

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        sys.exit(1)

    return window


if __name__ == "__main__":
    main()