document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".album-slider").forEach((slider) => {
        new Swiper(slider, {
            loop: true,
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
        });
    });
});
function openGalleryTab(tabName) {
    document.querySelectorAll('.gallery-tab-content').forEach((tab) => {
        tab.style.display = 'none'
    })
    document.getElementById(tabName).style.display = 'block'

    document.querySelectorAll('.gallery-tab-btn').forEach((btn) => {
        btn.classList.remove('active')
    })
    event.currentTarget.classList.add('active')
}
// document.getElementById('gallery-images').style.display = 'block'

function openVideoLightbox(videoUrl) {
    let lightbox = document.getElementById('video-lightbox');
    let lightboxVideo = document.getElementById('lightbox-video');

    // Chỉ hiển thị lightbox trước, chưa chạy video ngay
    lightbox.style.display = "flex";

    // Chờ 500ms sau khi lightbox hiển thị, mới load video
    setTimeout(() => {
        if (videoUrl.includes("watch?v=")) {
            videoUrl = videoUrl.replace("watch?v=", "embed/");
        }
        lightboxVideo.src = videoUrl + "?autoplay=1";
    }, 100);
}

function closeVideoLightbox() {
    let lightbox = document.getElementById('video-lightbox');
    let lightboxVideo = document.getElementById('lightbox-video');

    lightbox.style.display = "none";
    setTimeout(() => { lightboxVideo.src = ""; }, 100); // Đợi 300ms rồi reset URL để dừng video
}