import json

try:
    import numpy as np
except ImportError:
    print("[LOG] Numpy is not installed, you should not import this module.")
    np = None


# -------------------------- JSON Convert ----------------------------- #
# --------------------------------------------------------------------- #


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def np2json(arr, outpath):
    with open(outpath, 'w', encoding='utf-8') as f:
        json.dump(arr, f, ensure_ascii=False, indent=4, cls=NumpyEncoder)
