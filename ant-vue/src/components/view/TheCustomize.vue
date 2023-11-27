<template>
  <div class="table_content">
    <div class="table__header table__header_custom">
      <div class="table__header__name">
        <span style="font-size: 20px;">Customization</span>
      </div>
      <div class="table__header__btn">
        <button class="btn btn-cancel">Discard</button>
        <button class="btn btn-next">Save</button>
      </div>
    </div>
    <div class="table__header__name">
      <div class="table__container_data__table">
        <div style="display: flex; position: relative; flex-direction: row">
            <div class="loading"></div>
            <div style="display:flex; flex-direction: column; margin-bottom: 15px; width: 70% ">
              <!-- Genaral Configuration -->
              <div class="configuration">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none">
                  <g clip-path="url(#clip0_3_7052)">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
                  </g>
                  <defs>
                  <clipPath id="clip0_3_7052">
                  <rect width="12" height="12" fill="white"/>
                  </clipPath>
                  </defs>
                  </svg>
                  <span>General Configuration</span>
              </div>
              <div class="widget_title">
                <div class="widget">Widget Title</div>
                <input type="text" class="input-widget" v-model="widget_title">
              </div>
              <div style="display: flex; flex-direction: row; margin-top: 18px; align-items: center">
                <div style="display: flex; flex-direction: column ">
                  <div class="color">Title Color</div>
                  <div style="display: flex; margin-top: 15px; align-items: center; flex-direction: row" class="border-input width-input">
                      <div class="input-color">
                        <input type="color" v-model="title_color">
                      </div>
                      <input v-model="title_color" type="text" class="text-color">
                  </div>
                </div>
                <div style="display: flex; flex-direction: column; margin-left: 12px" class="select-font">
                  <div class="font-size">Title font size (px)</div>
                  <select v-model="title_font_size">
                      <option disabled value="">Please select one</option>
                      <option value="10px">Extra Small</option>
                      <option value="15px">Small</option>
                      <option value="20px">Medium</option>
                      <option value="25px">Large</option>
                      <option value="30px">Extra Large</option>
                  </select>
              </div>
              </div>
              <div class="widget_title">
                <div class="widget">Widget Description</div>
                <input type="text" class="input-widget" v-model="widget_description">
              </div>
              <div style="display: flex; flex-direction: row; margin-top: 18px; align-items: center">
                <div style="display: flex; flex-direction: column">
                  <div class="color">Description Color</div>
                  <div style="display: flex; margin-top: 15px; align-items: center; flex-direction: row" class="border-input width-input">
                      <div class="input-color">
                        <input type="color" v-model="description_color">
                      </div>
                      <input v-model="description_color" type="text" class="text-color">
                  </div>
                </div>
                <div style="display: flex; flex-direction: column; margin-left: 12px" class="select-font">
                  <div class="font-size">Description font size (px)</div>
                  <select v-model="description_font_size">
                      <option disabled value="">Please select one</option>
                      <option value="10px">Extra Small</option>
                      <option value="15px">Small</option>
                      <option value="20px">Medium</option>
                      <option value="25px">Large</option>
                      <option value="30px">Extra Large</option>
                  </select>
              </div>
              </div>
              <div class="configuration" style="margin-top: 30px;">
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none">
                  <g clip-path="url(#clip0_3_7052)">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
                  </g>
                  <defs>
                  <clipPath id="clip0_3_7052">
                  <rect width="12" height="12" fill="white"/>
                  </clipPath>
                  </defs>
                  </svg>
                  <span>Button Configuration</span>
              </div>
              <div class="widget_title">
                <div class="widget">Button Text</div>
                <input type="text" class="input-widget" v-model="btn_text">
              </div>
              <div style="display: flex; flex-direction: row; margin-top: 18px; align-items: center">
                <div style="display: flex; flex-direction: column">
                  <div class="color">Button Text Color</div>
                  <div style="display: flex; margin-top: 15px; align-items: center; flex-direction: row" class="border-input width-input">
                      <div class="input-color">
                        <input type="color" v-model="text_color">
                      </div>
                      <input v-model="text_color" type="text" class="text-color">
                  </div>
                </div>
                <div style="display: flex; flex-direction: column; margin-left: 12px" class="select-font">
                  <div class="color">Description Color</div>
                  <div style="display: flex; margin-top: 15px; align-items: center; flex-direction: row" class="border-input width-input  ">
                      <div class="input-color">
                        <input type="color" v-model="background_color">
                      </div>
                      <input v-model="background_color" type="text" class="text-color">
                  </div>
              </div>
              </div>
              <div style="display: flex; flex-direction: row; margin-top: 18px; align-items: center">
                <div style="display: flex; flex-direction: column">
                  <div class="color">Button border color</div>
                  <div style="display: flex; margin-top: 15px; align-items: center; flex-direction: row" class="border-input width-color">
                      <div class="input-color">
                        <input type="color" v-model="border_color">
                      </div>
                      <input v-model="border_color" type="text" class="text-color-button">
                  </div>
                </div>
              </div>
            </div>
            <div class="display: flex; position: relative; flex-direction: row">
              <div class="vertical-line"></div>
            </div>
            <div style="display: flex; position: relative; flex-direction: row; width:50%">
              <div style="display:flex; flex-direction: column; margin-bottom: 15px">
                <div class="configuration">
                  <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none">
                    <g clip-path="url(#clip0_3_7052)">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M0 6C0 2.6865 2.6865 0 6 0C9.3135 0 12 2.6865 12 6C12 9.3135 9.3135 12 6 12C2.6865 12 0 9.3135 0 6ZM6.67501 7.20115H5.39337V7.11654C5.39992 5.93719 5.68836 5.76447 6.21774 5.44746C6.27369 5.41396 6.33232 5.37885 6.3936 5.34077C6.83188 5.06548 7.16874 4.71775 7.16874 4.21065C7.16874 3.64197 6.72322 3.27251 6.16903 3.27251C5.6583 3.27251 5.1748 3.51123 5.1422 4.1922H3.78223C3.81845 2.81578 4.90852 2.1 6.17627 2.1C7.55994 2.1 8.51256 2.96825 8.51256 4.19254C8.51256 5.02202 8.09601 5.56534 7.42954 5.96378C7.37879 5.99491 7.33125 6.02353 7.28673 6.05034C6.81326 6.33539 6.68163 6.41464 6.67501 7.11654V7.20115ZM6.77747 9.00841C6.77384 9.45031 6.40801 9.80528 5.98059 9.80528C5.53869 9.80528 5.18009 9.45031 5.18372 9.00841C5.18009 8.57375 5.53869 8.21877 5.98059 8.21877C6.40801 8.21877 6.77384 8.57375 6.77747 9.00841Z" fill="#5C5F62"/>
                    </g>
                    <defs>
                    <clipPath id="clip0_3_7052">
                    <rect width="12" height="12" fill="white"/>
                    </clipPath>
                    </defs>
                    </svg>
                    <span>Preview</span>
                </div>
                <div class="table__container_data__preview">
                  <div class="preview">
                    <div class="text_preview">
                      <div class="text_preview_header" :style="{color: title_color, fontSize: title_font_size}">
                        {{ this.widget_title }}
                      </div>
                      <div class="text_preview_bottom" :style="{color: description_color, fontSize: description_font_size}">
                        {{ this.widget_description }}.
                      </div>
                    </div>
                    <div class="product_total">
                      <div class="product_item"
                      v-for="product in this.filteredRecommendation"
                      :key="product.id"
                      >
                        <img :src="product.url_img"
                        style="border: 1px solid #E2E2E2; border-radius: 5px; width: 65px; height: 65px"
                        :alt="product.name">
                      </div>
                      <div class="total" style="gap: 20px">
                        <div style="display: flex; gap: 10px; align-items: center">
                          <div class="total_text">Total</div>
                          <div class="total_price">${{ parseFloat(20).toFixed(2) }}</div>
                          <div class="total_discount">20$</div>
                        </div>
                        <button
                        :style="{ background: background_color, borderColor: border_color, color: text_color }"
                        class="btn-buynow">{{this.btn_text}}</button>
                      </div>
                    </div>
                    <div style="margin-top: 0px; margin-bottom: 17px">
                      <div style="display: flex; flex-direction: row; justify-content"
                      v-for="product in this.filteredRecommendation"
                             :key="product.id"
                      class="item"
                      >
                      <div class="product_name">
                        <input type="checkbox" class="name">
                        <div>{{ product.name }}</div>
                      </div>
                        <span style="color: red">${{ parseFloat(product.price).toFixed(2) }}</span>
                      </div>
                    </div>
                  </div>
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
  name: 'TheCustomize',
  data () {
    return {
      widget_description: 'Goods deals only for you',
      widget_title: 'YOU MAY ALSO LIKE...',
      title_color: '#000000',
      description_color: '#000000',
      description_font_size: '',
      background_color: '#000000',
      border_color: '#000000',
      btn_text: 'Buy now',
      list_ids: [],
      total_price: 0,
      total_compare_at_price: 0,
      text_color: '#ffffff',
      title_font_size: '',
      filteredRecommendation: [{
        id: 1,
        name: 'Chân người',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        id: 2,
        name: 'Vòng Tay',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        id: 3,
        name: 'Test',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      }]
    }
  }
}
</script>
<style lang="css" scoped>

.vertical-line {
  height: 97%; /* Chiều cao của đường kẻ dọc */
  border-left: 1px solid #BFBFBF; /* Đường kẻ dọc màu đen */
  transform: translate(-106px,10px);
}
.preview {
  gap: 20px
}

.product_total {
  display: flex;
  align-items: center;
  gap: 40px;
  justify-content: center
}

.total {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text_preview {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 6px;
  align-self: stretch;
}

.text_preview .text_preview_header {
  color: #000;
  text-align: center;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: 22px;
}

.text_preview .text_preview_bottom{
  color: #000;
  text-align: center;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 22px
}

.table__container_data__table{
  margin-right: 20px;
}

.table__container_data__preview {
  padding: 16px 20px;
  border: 1px solid #e2e2e2;
  background: #fff;
  margin-bottom: 30px;
  width: 100%;
  height: auto;
}

.table__header_custom {
  margin-top: 25px;
}

.btn {
  align-items: center;
  padding: 4px 12px;
  font-style: normal;
  gap: 4px;
  border-radius: 5px;
  font-size: 14px;
  line-height: 24px;
  cursor: pointer;
}

.btn-next {
  gap: 4px;
  width: 62px;
  height: 32px;
  color: white;
  font-weight: 700;
  border: #1D1E21;
  background: #1D1E21;

}

.btn-cancel {
  font-weight: 500;
  border: #E2E2E2;
  color: #000000;
  flex: none;
  order: 1;
  flex-grow: 0;
  width: 71px;
  height: 32px;
  background: #fff;
  margin-right: 25px;
}

.configuration {
  display: flex;
  align-items: center;
}

.configuration span {
  margin-left: 10px;
  color: #202223;
  height: 28px;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 28px;
}

.widget {
  height: 22px;
  margin-top: 25px;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 22px;
  color: black
}

.input-widget {
  background: white;
  border: 1px solid #E2E2E2;
  border-radius: 5px;
  height: 40px;
  margin-top: 10px;
  width: 77%;
  padding-left: 12px;
  padding-right: 12px;
}

.widget_title{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  align-self: stretch;
}

.color {
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  color: black;
  height: 22px;
  line-height: 22px
}

.text-color {
  background: white;
  height: 36px;
  border: none;
  gap: 10px;
  color: #202223;
  border-radius: 5px;
  width: 190px;
  outline: none;
  margin-right: 12px;
}

.text-color-button{
  background: white;
  height: 36px;
  border: none;
  gap: 10px;
  color: #202223;
  border-radius: 5px;
  width: 250px;
  outline: none;
  margin-right: 12px;
}

.border {
  width: 50%;
}

.font-size {
  color: black;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 22px;
  height: 22px;
}

.select-font select {
  background: white;
  border: 1px solid #C9CCCF;
  border-radius: 5px;
  height: 41px;
  margin-top: 15px;
  width: 346px;
}

.input-color {
  width: 30px;
  overflow: hidden;
  height: 21px;
  margin: 9px 12px 9px 12px;
}

.input-color > input {
  width: 200%;
  height: 200%;
  cursor: pointer;
  margin-top: -15px;
  margin-left: -15px;
  border: none;
}

.border-input {
  border-radius: 6px;
  border: 1px solid #939393;
}
.input-length{
  width: 32%;
}

.preview {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.total_text {
  color: #000;
  text-align: center;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px; /* 137.5% */
}

.total_price {
  color: #F00;
  text-align: center;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px; /* 137.5% */
}

.total_discount {
  color: #848484;
  text-align: center;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px; /* 137.5% */
  text-decoration-line: strikethrough;
}

.total > button {
  display: flex;
  width: 157px;
  padding: 4px 12px;
  justify-content: center;
  align-items: center;
  gap: 10px;
  border-radius: 6px;
  border: 1px solid #1890FF;
  background: #1890FF;
}

.btn-buynow {
  color: #FFF;
  text-align: center;
  font-size: 14px;
  font-style: normal;
  font-weight: 600;
  line-height: 20px; /* 142.857% */
}

.product_name{
  display: flex;
  align-items: center;
}

.item {
  height: 16px;
  align-items: center;
  margin-top: 12px;
}

.item .product_name input {
  width: 16px;
  background: white;
  border-radius: 2px;
  margin-left: 30px;
}

.item > span {
  color: #F00;
  font-size: 12px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px;
  margin-right: 84px;
  margin-left: auto;
}

.width-input {
  width: 345px;
}

.width-color {
  width: 220%;
}

</style>
