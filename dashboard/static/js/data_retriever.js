'use strict';

export default class DataRetriever {

    constructor() {

    }

    static get DATA_UPDATED_EVENT() { return 'DATA_UPDATED_EVENT'}

    start() {
        setTimeout(this._fetch, 5 * 1000);
    }

    _fetch() {
        dispatchEvent(new Event(DataRetriever.DATA_UPDATED_EVENT));
    }
}

