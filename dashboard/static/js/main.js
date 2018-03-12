'use strict';

import MapController from './map_controller.js';
import App from './app.js';
import DataRetriever from "./data_retriever.js";


new App();
new MapController();

let dataRetriever = new DataRetriever();
dataRetriever.start();



