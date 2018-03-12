'use strict';

import * as map from './map.js';

let selectedIndex = 0;
let views = null;
let barItems = null;
let headerTitle = null;
let titles = ['Station', 'Emission', 'Monitor', 'About'];

window.onload = () => {
    init();
    map.loadMap();
    addListeners();
};

function init() {
    views = document.getElementsByClassName('view');
    barItems = document.getElementsByClassName('sidebar-item');
    headerTitle = document.getElementById('header-title');

    barItems[selectedIndex].style.backgroundColor = '#fff';
    barItems[selectedIndex].style.color = '#e8491d';
    for (let view of views) {
        view.style.visibility = 'hidden';
    }
    views[selectedIndex].style.visibility = 'visible';
}

function addListeners() {
    for (let item of barItems) {
        item.addEventListener('mouseup', function(event) {
            let target = event.target;
            if (target === barItems[selectedIndex]){ return; }
            let idx = [].indexOf.call(barItems, target);

            target.style.backgroundColor = '#fff';
            target.style.color = '#e8491d';
            barItems[selectedIndex].style.backgroundColor = '#f2f4f6';
            barItems[selectedIndex].style.color = '#000';
            views[selectedIndex].style.visibility = 'hidden';
            views[idx].style.visibility = 'visible';
            headerTitle.innerHTML = titles[idx];

            selectedIndex = [].indexOf.call(barItems, target);
        });
        item.addEventListener('mouseenter', function(event) {
            if (event.target === barItems[selectedIndex]){ return; }
            event.target.style.color = '#e8491d';
        });
        item.addEventListener('mouseout', function(event) {
            if (event.target === barItems[selectedIndex]){ return; }
            event.target.style.color = '#000';
        })
    }
}
