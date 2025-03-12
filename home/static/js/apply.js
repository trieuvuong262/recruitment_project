document.addEventListener("DOMContentLoaded", function () {
    // Lấy các phần tử form
    const citySelect = document.getElementById("city");
    const districtSelect = document.getElementById("district");
    const wardSelect = document.getElementById("ward");
    const phoneInput = document.getElementById("phone");
    const dobInput = document.getElementById("dob");
    const cvInput = document.getElementById("cv-input");
    const cvFileName = document.getElementById("cv-file-name");
    const portraitInput = document.getElementById("portrait-input");
    const portraitFileName = document.getElementById("portrait-file-name");

    // 🔹 Lấy danh sách tỉnh/thành phố
    if (citySelect) {
        fetch("https://provinces.open-api.vn/api/?depth=1")
            .then(response => response.json())
            .then(data => {
                data.forEach(city => {
                    let option = new Option(city.name, city.code);
                    citySelect.add(option);
                });
            });

        // Khi chọn Tỉnh/Thành phố, tải danh sách Quận/Huyện
        citySelect.addEventListener("change", function () {
            let cityCode = this.value;
            if (districtSelect) {
                districtSelect.innerHTML = '<option value="">Chọn quận/huyện</option>';
                wardSelect.innerHTML = '<option value="">Chọn xã/phường</option>';
                wardSelect.disabled = true;

                if (cityCode) {
                    districtSelect.disabled = false;
                    fetch(`https://provinces.open-api.vn/api/p/${cityCode}?depth=2`)
                        .then(response => response.json())
                        .then(data => {
                            data.districts.forEach(district => {
                                let option = new Option(district.name, district.code);
                                districtSelect.add(option);
                            });
                        });
                } else {
                    districtSelect.disabled = true;
                }
            }
        });
    }

    // Khi chọn Quận/Huyện, tải danh sách Xã/Phường
    if (districtSelect && wardSelect) {
        districtSelect.addEventListener("change", function () {
            let districtCode = this.value;
            wardSelect.innerHTML = '<option value="">Chọn xã/phường</option>';

            if (districtCode) {
                wardSelect.disabled = false;
                fetch(`https://provinces.open-api.vn/api/d/${districtCode}?depth=2`)
                    .then(response => response.json())
                    .then(data => {
                        data.wards.forEach(ward => {
                            let option = new Option(ward.name, ward.code);
                            wardSelect.add(option);
                        });
                    });
            } else {
                wardSelect.disabled = true;
            }
        });
    }

    // 🔹 Kiểm tra số điện thoại
    if (phoneInput) {
        phoneInput.addEventListener("blur", function () {
            let phonePattern = /^0\d{9}$/;
            if (!phonePattern.test(phoneInput.value)) {
                alert("Số điện thoại không hợp lệ!");
                phoneInput.value = "";
            }
        });
    }

    // 🔹 Kiểm tra ngày sinh (18 - 70 tuổi)
    if (dobInput) {
        let today = new Date();
        let minDate = new Date(today.getFullYear() - 70, today.getMonth(), today.getDate());
        let maxDate = new Date(today.getFullYear() - 18, today.getMonth(), today.getDate());

        dobInput.setAttribute("min", minDate.toISOString().split("T")[0]);
        dobInput.setAttribute("max", maxDate.toISOString().split("T")[0]);

        dobInput.addEventListener("blur", function () {
            let selectedDate = new Date(dobInput.value);
            if (selectedDate > maxDate || selectedDate < minDate) {
                alert("Vui lòng nhập ngày sinh hợp lệ!");
                dobInput.value = "";
            }
        });
    }

    // 🔹 Xử lý file CV
    if (cvInput && cvFileName) {
        cvInput.addEventListener("change", function () {
            cvFileName.textContent = this.files[0] ? this.files[0].name : "Chưa có tệp nào được chọn";
        });
    }

    // 🔹 Xử lý file ảnh chân dung
    if (portraitInput && portraitFileName) {
        portraitInput.addEventListener("change", function () {
            portraitFileName.textContent = this.files[0] ? this.files[0].name : "Chưa có tệp nào được chọn";
        });
    }
});
