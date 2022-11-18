from __future__ import print_function

import argparse

import neuroglancer
import neuroglancer.cli
import time

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    neuroglancer.cli.add_server_arguments(ap)
    args = ap.parse_args()
    neuroglancer.cli.handle_server_arguments(args)
    viewer = neuroglancer.Viewer()
    with viewer.txn() as s:
        s.layers["image"] = neuroglancer.ImageLayer(
            source="precomputed://gs://neuroglancer-public-data/flyem_fib-25/image"
        )
        s.layers["image2"] = neuroglancer.ImageLayer(
            source="n5://s3://janelia-cosem-datasets/jrc_mus-liver/jrc_mus-liver.n5/em/fibsem-uint8"
        )
    print(viewer)
    time.sleep(1000)
