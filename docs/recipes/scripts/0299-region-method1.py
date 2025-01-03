from iiif_prezi3 import Manifest, ResourceItem, SelectorItem3, AnnotationPage, Annotation, config, SpecificResource

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"
base_url = "https://iiif.io/api/cookbook/recipe/0299-region"

manifest = Manifest(
    id=f"{base_url}/manifest.json",
    label="Berliner Tageblatt article, 'Ein neuer Sicherungsplan?'"
)

anno_page = AnnotationPage(
    id=f"{base_url}/page/p1/1"
)
selector = SelectorItem3(
    type="ImageApiSelector"
)
image_source = ResourceItem(
    id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2/full/max/0/default.jpg",
    type="Image",
    format="image/jpeg",
    height=4999,
    width=3536,
)
image_source.make_service(
    id="https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2",
    type="ImageService3",
    profile="level1"
)
temp_source = {
                  "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2/full/max/0/default.jpg",
                  "type": "Image",
                  "format": "image/jpeg",
                  "height": 4999,
                  "width": 3536,
                  "service": [
                    {
                      "id": "https://iiif.io/api/image/3.0/example/reference/4ce82cef49fb16798f4c2440307c3d6f-newspaper-p2",
                      "profile": "level1",
                      "type": "ImageService3"
                    }
                  ]
                }
temp_selector = {
                  "@context": "http://iiif.io/api/annex/openannotation/context.json",
                  "type": "ImageApiSelector",
                  "region": "1768,2423,1768,2080"
                }
anno_body = SpecificResource(
    id=f"{base_url}/body/b1",
    type="SpecificResource",
    format="image/jpeg",
    source=image_source,
    selector=temp_selector,
)
# print(anno_body.json(indent=2))
canvas = manifest.make_canvas(
    id=f"{base_url}/canvas/p1",
)
anno = Annotation(
    id=f"{base_url}/annotation/p0001-image",
    motivation="painting",
    body=anno_body,
    target=canvas.id
)
anno_page.add_item(anno)
# print(anno_page.json(indent=2))
canvas.add_item(anno_page)

print(manifest.json(indent=2))
