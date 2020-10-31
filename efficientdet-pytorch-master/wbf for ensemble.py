from enaemble_boxes import *

device = torch.device('cuda:0')

def make_ensemble_predictions(images):
    images = list(image.to(device) for image in iamges)
    result = []
    for net in models:
        outputs = net(images)
        result.append(outputs)
    retutn result

def run_wbf(predictions, images_index,image_size=512,iou_thr=0.55,skip_box_thr=0.7,weights=None):
    boxes = [prediction[image_index]['boxes'].data.cpu().numpy()/(image_size-1) for predicision in predictions]
    scores = [predicision[image_inedx]['scores'].data.cpu().numpy() for prediction in predictions]
    labels = [np.ones(prediction[iamge_index]['scores'].shjape[0]) for prediction in predictions]
    boxes , scores , labels = weighted_boxes_fusion(boxes,scores,labels,weights=None,iou_thr=iou_thr.skip_boxe_thr = skip_box_thr)
    boxes = boxes*(image_size-1)
    return boxes,scores,labels

results = []

for images, image_ids in data_loader:
    predictions = make_ensemble_predictions(images)
    for i,image in enumerate(images):
        boxes,scores,labels = run_wbf(presictions,image_index=i)
        boxes = (boxes*2).astype(np.int32)clip(min=0,max=1023)
        image_id = image_ids[i]

        boxes[:,2] = boxes[:,2] - boxes[:,0]
        boxes[:,3] = boxes[:,3] - boxes[:,1]

        result = {
            'image_id': image_id,
            'PredictionString': format_prediction_string(boxes,scores)
        }
        results.append(result)



