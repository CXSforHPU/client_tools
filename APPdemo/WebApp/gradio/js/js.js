document.addEventListener("DOMContentLoaded", function () {
    // 图片上传时，添加加载动画
    let uploadButtons = document.querySelectorAll("button#submit_button");

    uploadButtons.forEach(button => {
        button.addEventListener("click", function () {
            button.innerHTML = "处理中...";
            button.style.backgroundColor = "#007a7f";

            // 模拟加载延迟
            setTimeout(() => {
                button.innerHTML = "提交";
                button.style.backgroundColor = "#00adb5";
            }, 2000);  // 2秒模拟加载时间
        });
    });

    // 添加 hover 动画到按钮
    let chatbotSubmit = document.querySelectorAll(".chatbot #submit_button");
    chatbotSubmit.forEach(button => {
        button.addEventListener("mouseover", function () {
            button.style.transform = "scale(1.05)";
        });
        button.addEventListener("mouseout", function () {
            button.style.transform = "scale(1)";
        });
    });
});
