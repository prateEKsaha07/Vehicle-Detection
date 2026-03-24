### Still in development will upload the full version soon

## Did the initial testing these are results

Ultralytics 8.4.26  Python-3.12.2 torch-2.11.0+cpu CPU (AMD Ryzen 5 5600G with Radeon Graphics)
Model summary (fused): 73 layers, 3,006,233 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 19/19 2.5s/it 46.7s
                   all        598       1981      0.648      0.383      0.399      0.286
                   car        329        850      0.697      0.686      0.698      0.523
                   car        329        850      0.697      0.686      0.698      0.523
                  bike        447        971      0.758      0.282      0.335      0.209
                 truck        140        160      0.489      0.181      0.166      0.125
Speed: 1.9ms preprocess, 63.4ms inference, 0.0ms loss, 3.4ms postprocess per image
Results saved to D:\2DOD\Vehicle Detection\runs\detect\train