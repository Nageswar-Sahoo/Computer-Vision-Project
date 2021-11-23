template/
│
├── main.py - main script to start training
├── config.json - holds configuration for training
├── base/ - abstract base classes
│   ├── base_data_loader.py
│   ├── base_model.py
│   └── base_trainer.py
│
├── data_loader/ - anything about data loading goes here
│   └── data_loaders.py
│
├── data/ - default directory for storing input data
│
├── model/ - models, losses, and metrics
│   ├── model.py
│   ├── metric.py
│   └── loss.py
│
├── saved/
│   ├── models/ - trained models are saved here
│   └── log/ - default logdir for tensorboard and logging output
│
├── trainer/ - trainers hold code detial for training ans testing 
│   └── trainer.py
│
├── logger/ - module for tensorboard logging
│   ├── visualization.py
│   ├── logger.py
│   └── logger_config.json
│  
└── utils/ - small utility functions
    ├── util.py
	├── base_came.py
	├── grade_cam.py
	├── image.py
	├── activations_and_gradients.py