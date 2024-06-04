from bing_image_downloader.downloader import download

query_string = 'Rhabdophis tigrinus'

download(query_string, limit=500, output_dir='dataset_2', adult_filter_off=True,
         force_replace=False, timeout=5, verbose=True, filter='jpg')