<template>
  <div class="table__content">
    <div class="table__header table__header_install">
      <div class="table__header__name">
        <span style=" font-size: 20px;">Installation Guide</span>
      </div>
      <div class="installation-btn">
        <button class="m-btn" id="btn-themes" @click="handleThemeCustomization">Go to Themes Customization</button>
      </div>
    </div>
    <div class="table__container">
      <div class="table__container__wapper">
        <div class="table__container_data__table">
          <div class="common_content">
            <div class="common_content_up">
              <div class="data_congratulation">CONGRATULATION! YOU HAVE CREATED WIDGET SUCCESSFULLY!</div>
              <div class="data_follow">Now please follow these steps below to display it on your product pages</div>
            </div>
            <div class="data_content">
              <p>1. Lorem ipsum is placeholder text commonly used in the graphic, print</p>
              <p>2. and publishing industries for previewing layouts and visual mockups.</p>
              <p>3. Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for
                  previewing layouts and visual mockups.</p>
            </div>
            <div class="frame_video">
              <div class="data_video">
                <video controls height="70%" width="70%">
                  <source src="../../assets/video/test.mp4" type="video/mp4">
              </video>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TheInstallation'
}
</script>
<style lang="css" scoped>

.table__container_data__table {
  height: calc(100vh - 30%);
}
.installation-btn{
  margin-right: 24px;
}
.common_content{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 36px;
}

.common_content .common_content_up {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.table__header_install{
  margin-top: 25px;
}
.data_congratulation{
  font-style: normal;
  font-weight: 700;
  text-align: center;
  font-size: 20px;
  line-height: 22px;
  color: black;
}

.data_content {
  width: 48%;
}
.data_content p {
  color: #000;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 22px;
}

.data_follow {
  color: #000;

  font-size: 14px;
  font-style: normal;
  font-weight: 700;
  line-height: 22px; /* 157.143% */
}

.frame_video {
  display: flex;
  width: 70%;
  height: auto;
  justify-content: center;
  align-items: center;
  margin-bottom: 50px;
  gap: 10px
}
.data_video {
  display: flex;
  width: 70%;
  padding: 20px;
  justify-content: center;
  align-items: center;
}

</style>
