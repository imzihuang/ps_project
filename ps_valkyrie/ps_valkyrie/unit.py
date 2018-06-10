# -*- coding: utf-8 -*-

import json

def unit_data(self, body):
    result = {}
    content_rating = body.get("include")[0].get("attributes", {}).get("content-rating", {}).get("rating-system", "")
    file_size_dic = body.get("include")[0].get("attributes", {}).get("file-size",None)
    file_size = file_size_dic.get("value", "") + file_size_dic.get("unit", "") if file_size_dic else ""
    game_content_type = body.get("include")[0].get("attributes", {}).get("game-content-type", "")
    genres = ",".join(body.get("include")[0].get("attributes", {}).get("genres"))
    long_description = body.get("include")[0].get("attributes", {}).get("long-description", "")
    media_list = body.get("include")[0].get("attributes", {}).get("media-list", {})
    name = body.get("include")[0].get("attributes", {}).get("name", "")
    parent = body.get("include")[0].get("attributes", {}).get("parent", {})
    platforms = ",".join(body.get("include")[0].get("attributes", {}).get("platforms"))
    plus_reward_description = body.get("include")[0].get("attributes", {}).get("plus-reward-description", "")
    provide_name = body.get("include")[0].get("attributes", {}).get("provide-name", "")
    ps_camera_compatibility = body.get("include")[0].get("attributes", {}).get("ps-camera-compatibility", "incompatible")
    ps_vr_compatibility = body.get("include")[0].get("attributes", {}).get("ps-vr-compatibility", "incompatible")
    release_date = body.get("include")[0].get("attributes", {}).get("release-date", "0000-00-00T01:00:00Z")
    skus = body.get("include")[0].get("attributes", {}).get("skus", [])
    star_rating = body.get("include")[0].get("attributes", {}).get("star-rating", {})
    subtitle_language_codes = ",".join(body.get("include")[0].get("attributes", {}).get("subtitle_language_codes"))
    voice_language_codes = ",".join(body.get("include")[0].get("attributes", {}).get("voice-language-codes"))
    thumbnail_url_base = body.get("include")[0].get("attributes", {}).get("thumbnail-url-base", "")
    upsell_info = body.get("include")[0].get("attributes", {}).get("upsell-info", "")

    result.update({
        "content_rating": content_rating,
        "file_size": file_size,
        "game_content_type": game_content_type,
        "genres": genres,
        "long_description": long_description,
        "media_list": media_list,
        "name": name,
        "parent": parent,
        "platforms": platforms,
        "plus_reward_description": plus_reward_description,
        "provide_name": provide_name,
        "ps_camera_compatibility": ps_camera_compatibility,
        "ps_vr_compatibility": ps_vr_compatibility,
        "release_date": release_date,
        "skus": skus,
        "star_rating": star_rating,
        "subtitle_language_codes": subtitle_language_codes,
        "voice_language_codes": voice_language_codes,
        "thumbnail_url_base": thumbnail_url_base,
        "upsell_info": upsell_info
    })
    return result




