def get_config_property(prop_name):
    return getattr(Config, prop_name, None)


class Config:
    ### Global config
    AUTHOR = None
    TORCH_DEVICE = 'cuda'  # 'cpu' if no GPU is available
    OUTPUT_DIR = None  # Set to None by default; users will provide their own

    TIME_ZONE = -4  # Relative to UTC time
    ALGO_TYPE = None
    ALGO_NAME = None

    ### Default parameters
    SEED = 0
    STEPS = 5
    PROMPT = "a scenic landscape"

    ### Automatic variables
    IMAGE_NAME = None
    IMAGE_PATH = None
    STEP_COUNT = None
    STEP_CURRENT = None

    ### GIF Settings
    FPS = 6

    ### Params image settings
    TXT_IMG_WIDTH = 1024
    TXT_IMG_HEIGHT = 768
    TXT_IMG_MARGIN = 0
    TXT_DARK_MODE = False
    TXT_COLOR_LIGHT = 'black'
    TXT_COLOR_DARK = 'white'
    TXT_COLOR_MID = 'gray'
    TXT_FONT_SIZE = 44
    TXT_MAX_LINELENGTH = 46
    TXT_FONT = "Futura"

    @staticmethod
    def check():
        settings_to_check = [
            'PROMPT',
            'AUTHOR',
            'ALGO_TYPE',
            'ALGO_NAME',
            'OUTPUT_DIR'
        ]
        for prop_name in settings_to_check:
            prop = get_config_property(prop_name)
            if prop is None:
                raise Exception(f'Config.{prop_name} needs to be set.')
        print('Config OK.')

    @staticmethod
    def set_output_dir(custom_output_dir=None):
        if custom_output_dir:
            Config.OUTPUT_DIR = custom_output_dir
        else:
            user_dir = input("Enter the directory path to save outputs (or press Enter to use default): ").strip()
            if user_dir:
                Config.OUTPUT_DIR = user_dir
            else:
                Config.OUTPUT_DIR = '/content/drive/MyDrive/ARCH 393 UW/Workshop/Diffusion Models/Outputs'
        print(f"Output directory set to: {Config.OUTPUT_DIR}")

    @staticmethod
    def to_dict():
        return {
            'output_dir': Config.OUTPUT_DIR,
            'torch_device': Config.TORCH_DEVICE,
            'author': Config.AUTHOR,
            'image_name': Config.IMAGE_NAME,
            'image_path': Config.IMAGE_PATH,
            'prompt': Config.PROMPT,
            'seed': Config.SEED,
            'fps': Config.FPS
        }
