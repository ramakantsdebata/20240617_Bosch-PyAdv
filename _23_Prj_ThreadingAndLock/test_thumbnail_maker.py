

## Run this test from the parent folder as
# pytest _00_BaseCode/.

from thumbnail_maker import ThumbnailMakerService
# import thumbnail_maker

IMG_URLS = \
    [
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_01.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_02.jpeg',
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_03.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_04.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_05.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_06.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_07.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_08.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_09.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_10.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_11.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_12.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_13.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_14.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_15.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_16.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_17.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_18.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_19.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_20.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_21.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_22.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_23.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_24.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_25.jpeg', 
    'https://gitlab.com/public-access-rsd/images/-/raw/main/Image_26.jpeg'
    ]
    
def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)

