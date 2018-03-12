'use strict';

export default class App {

    constructor() {
        this.selectedIndex = 0;
        this.titles = ['Station', 'Emission', 'Monitor', 'About'];
        this.views = document.getElementsByClassName('view');
        this.barItems = document.getElementsByClassName('sidebar-item');
        this.headerTitle = document.getElementById('header-title');

        this.barItems[this.selectedIndex].style.backgroundColor = '#fff';
        this.barItems[this.selectedIndex].style.color = '#e8491d';
        for (let view of this.views) {
            view.style.visibility = 'hidden';
        }
        this.views[this.selectedIndex].style.visibility = 'visible';

        this.addListeners();
    }

    addListeners() {
        for (let item of this.barItems) {
            item.addEventListener('mouseup', (event) => {
                let target = event.target;
                if (target === this.barItems[this.selectedIndex]) {
                    return;
                }
                let idx = [].indexOf.call(this.barItems, target);

                target.style.backgroundColor = '#fff';
                target.style.color = '#e8491d';
                this.barItems[this.selectedIndex].style.backgroundColor = '#f2f4f6';
                this.barItems[this.selectedIndex].style.color = '#000';
                this.views[this.selectedIndex].style.visibility = 'hidden';
                this.views[idx].style.visibility = 'visible';
                this.headerTitle.innerHTML = this.titles[idx];

                this.selectedIndex = [].indexOf.call(this.barItems, target);
            });
            item.addEventListener('mouseenter', (event) => {
                if (event.target === this.barItems[this.selectedIndex]) {
                    return;
                }
                event.target.style.color = '#e8491d';
            });
            item.addEventListener('mouseout', (event) => {
                if (event.target === this.barItems[this.selectedIndex]) {
                    return;
                }
                event.target.style.color = '#000';
            })
        }
    }
}