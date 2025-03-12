document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".job-home-filter-tab");
    const contents = document.querySelectorAll(".job-home-filter-tab-content");

    tabs.forEach(tab => {
        tab.addEventListener("click", function () {
            tabs.forEach(t => t.classList.remove("active"));
            contents.forEach(c => c.classList.remove("active"));

            this.classList.add("active");
            document.getElementById(this.dataset.tab).classList.add("active");
            
        });
        
    });
    
    
});
