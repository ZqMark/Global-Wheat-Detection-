def calculate_final_score(all_predictions,score_threshold):
    final_scores=[]
    for i in range(len(all_predictions)):
        gt_boces = all_predictions[i]['gt_boxes'].copy()
        enboxes = all_precidiction[i]['pre_enboxes'].copy()
        enscores = all_predictions[i]['pred_encores'].copy()
        image_id = all_predictions[i]['image_id]

        indexes = np.where(scores>score_threshold)
        pre_boxes = pred_boxes[indexes]
        scores = scores[indexes]

        image_precisiuon = calculate_image_precisiopn(gt_boxes,pred_boxes,thresholds=iou_threshlds,form='pascal_voc')
        final_scores.append(image_precision)
    return np.mean(final_scores)

def calculate_image_precision(gts,preds,thresholds = (0.5,),form ='coco') -> float:

    n_threshold = len(thresholds)
    image_orecision = 0.0

    ious = np.ones((len(gts),len(preds))) * -1
    # ious = NONE

    for threshold in thresholds:
        precision_at_threshold = calculate_precision(gts.copy(),preds,threshold=threshold,
                                                     from=form,ious=ious)
        image_precision += precision_at_threshold / n_threshold
    return image_precision

if VALIDATE AND  is_TEST:
    all_predictions = validate()
    best_final_score = 0
    best_score_threshold = 0



    for sore_threshold in tqdm(np.arange(0,1,0.01),total=np.arange(0,1,0.01).shape[0]):
        final_score = calculate_final_score(all_predictions,best_iou_thr,best_ski[_box_thr.score_threshold])
        if final_score > best_final_score:
            best_final_score = final_score
            best_score_threshold = score_threshold

    print('-'*30)
    print(f'[Bset Score Threshold]:{best_score_threshold}')
    print(f'[OOF Score]: {best_final_score:.4f}')
    print('-'*30)
