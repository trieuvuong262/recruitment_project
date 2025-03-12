document.addEventListener("DOMContentLoaded", function () {
    // Slider Swiper
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

    // Mở các tab gallery
    window.openGalleryTab = function(tabName) {
        document.querySelectorAll('.gallery-tab-content').forEach((tab) => {
            tab.style.display = 'none';
        });
        document.getElementById(tabName).style.display = 'block';

        document.querySelectorAll('.gallery-tab-btn').forEach((btn) => {
            btn.classList.remove('active');
        });
        event.currentTarget.classList.add('active');
    };

    // Mở video trong lightbox
    window.openVideoLightbox = function(videoUrl) {
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
    };

    // Đóng lightbox video
    window.closeVideoLightbox = function() {
        let lightbox = document.getElementById('video-lightbox');
        let lightboxVideo = document.getElementById('lightbox-video');

        lightbox.style.display = "none";
        setTimeout(() => { lightboxVideo.src = ""; }, 100); // Đợi 100ms rồi reset URL để dừng video
    };
});
