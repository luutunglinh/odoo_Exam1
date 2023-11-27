<template>
  <div style="position: relative; width: 100%">
    <div class="choose-recommendation-product" style="height: 336px">
      <div class="choose-recomendation">
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
        <span>Choose recomendation products</span>
      </div>
      <div class="search">
        <!-- <Input size="large" @search="onSearch" v-model="search_recommendation" placeholder="Search product by name"
          :addon-after="this.list_recommendation.length + ' selected' "/> -->
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M11.25 11.25L14.25 14.25" stroke="#868B90" stroke-width="1.5" stroke-linecap="round" stroke-lsearch-boxnejoin="round"/>
            <path d="M7.5 12.25C10.1234 12.25 12.25 10.1234 12.25 7.5C12.25 4.87665 10.1234 2.75 7.5 2.75C4.87665 2.75 2.75 4.87665 2.75 7.5C2.75 10.1234 4.87665 12.25 7.5 12.25Z" stroke="#868B90" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          <AutoComplete
                  v-model:value="searchValue"
                  :bordered="false"
                  placeholder="Search product by name"
                  @search="onSearch"
                  @focus="onFocus"
                  @blur="onBlur"
                  size="large"
                  class="input"
              />
              <div class="search-box" v-if="isSearch">
                  <div class="search-box-item" v-for="product in data_Search" :key="product.id" @click="addProduct(product)">
                      <div >
                          <img :src="product.url_img"/>
                          <div>
                              <span class="title"> {{ product.name }} </span>
                              <span class="des">$ {{product.price}}</span>
                          </div>
                      </div>
                </div>
              </div>
              <div class="selected">
                <div style="padding-bottom: 3px">{{ selectedRowsCount }} selected</div>
              </div>
      </div>
      <div @click="deleteProducts" v-if="isDeleteShow"  class="remove-btn">Remove selected product(s)</div>
      <div class="table-product">
        <Table :columns="columns" :data-source="selected_product" :row-selection="rowSelection" :rowClassName="enable_widget ? '' : 'disabled-row '"
        :pagination="false"
        style="width: 100%;" size="small" class="test" styles="position: sticky;"
        >
            <template #headerCell="{ title }">
                <template v-if="title">
                  <strong>{{ title }}</strong>
                </template>
            </template>
            <template #bodyCell="{column, record}">
              <template v-if="column.key === 'url_img'">
                <img :src="record.url_img" :alt="record.name" style="'opacity: 0.2; width: 30px; height: 30px' ">
              </template>
              <template v-if="column.key === 'price'">
                ${{ record.price }}
              </template>
              <template v-if="column.key === 'compare_at_price'">
                  ${{ record.compare_at_price }}
              </template>
            </template>
      </Table>
      </div>
    </div>
  </div>

</template>
<script>
import { AutoComplete, Switch, Empty, Table } from 'ant-design-vue'
import { SearchOutlined } from '@ant-design/icons-vue'
export default {
  name: 'TheStoreProduct',
  components: {
    AutoComplete,
    Table
  },
  data () {
    return {
      content: '',
      showToast: false,
      watchFilter: false,
      isDeleteShow: false,
      searchValue: '',
      isSearch: false,
      enable_widget: true,
      tickAllRecommendation: false,
      selectedRowKeys: [],
      selected_product: [],
      columns: [
        {
          key: 'url_img',
          title: 'Image',
          dataIndex: 'url_img'
        },
        {
          key: 'name',
          title: 'Product Name',
          dataIndex: 'name'
        },
        {
          key: 'price',
          title: 'Price',
          dataIndex: 'price'
        },
        {
          key: 'compare_at_price',
          title: 'Compare at price',
          dataIndex: 'compare_at_price'
        },
        {
          title: 'In Stock',
          dataIndex: 'qty',
          key: 'qty'
        }
      ],
      isSelectAll: false,
      filteredRecommendation: [{
        key: 1,
        name: 'Test1',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        key: 2,
        name: 'Test2',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        key: 3,
        name: 'Test3',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        key: 4,
        name: 'Test4',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        key: 5,
        name: 'Test5',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      },
      {
        key: 6,
        name: 'Test6',
        price: 20000,
        qty: 20,
        compare_at_price: 20,
        url_img: 'https://source.unsplash.com/random/200x200?sig=1'
      }]
    }
  },
  created () {
    this.refreshTable()
  },
  methods: {
    onSelectChange (selectedRowKeys) {
      this.selectedRowKeys = selectedRowKeys
    },
    onSelectRow (record, selected, selectedRows, nativeEvent) {
      this.selectedRowKeys = selected ? [...this.selectedRowKeys, record.key] : this.selectedRowKeys.filter(key => key !== record.key)
      console.log('t', this.selectedRowKeys)
      if (this.selectedRowKeys.length < 1) {
        this.isDeleteShow = false
      } else {
        this.isDeleteShow = true
      }
    },
    onSelectAllRows (selected, selectedRows, changeRows) {
      // const rows = []
      // if (selected) {
      //   // Nếu là deselect tất cả, thì đặt lại selectedRowKey
      //   this.isDeleteShow = true
      //   this.rows = selectedRows
      // } else {
      //   this.isDeleteShow = false
      //   this.rows = []
      // }
      this.isSelectAll = selected
      console.log(selected, selectedRows)
      if (!selected) {
        // Nếu là deselect tất cả, thì đặt lại selectedRowKeys
        this.selectedRows = []
        this.isDeleteShow = false
      } else this.isDeleteShow = true
    },
    deleteProducts () {
      this.selected_product = this.selected_product.filter(record => !this.selectedRowKeys.includes(record.key))
      this.selectedRowKeys = []
      this.isDeleteShow = false
    },
    refreshTable () {
      if (this.filteredRecommendation.length < 0) {
        this.watchFilter = false
      } else this.watchFilter = true
    },
    onSearch (searchText) {
      this.data_Search = this.filteredRecommendation.filter(product => product.name.toLowerCase().includes(searchText))
    },
    onBlur () {
      this.isSearch = false
    },
    onFocus () {
      this.isSearch = true
    },
    addProduct (data) {
      // const lastNumber = parseInt(data.name.match(/\d+$/)[0])
      if ((this.selected_product.length < 6)) {
        // const newName = data.name.replace(/\d+$/, lastNumber + 1)
        // if ((!this.selected_product.some(product => product.key === data.key))) {}
        const dataSelectedProducts = {
          key: data.key,
          name: data.name,
          price: data.price,
          qty: data.qty,
          compare_at_price: data.compare_at_price,
          url_img: data.url_img
        }
        this.selected_product.push(dataSelectedProducts)
      } else {
        this.showToast = true
        this.content = 'You have reach the product limitation. Please remove any products from the list to continue selecting'
        setTimeout((e) => {
          this.showToast = false
        }, 3000)
      }
    }
  },
  computed: {
    rowSelection () {
      return {
        selectedRowKeys: this.selectedRowKeys,
        onChange: this.onSelectChange,
        onSelect: this.onSelectRow,
        onSelectAll: this.onSelectAllRows
      }
    },
    selectedRowsCount () {
      return this.selectedRowKeys.length
    }
  }

}
</script>
<style lang="css" scoped>

.input {
  display: flex;
  align-items: center;
  padding-left: 20px;
  border: 1.21px solid #E6E6E6;
  border-radius: 6px 0px 0px 6px;
  width: 100%;
}

.search .ant-input-group-addon {
  background-color: #fff;
}

.choose-recommendation-product {
  border: 1px solid #E2E2E2;
  background-color: white;
  margin-left: 20px;
  margin-right: 20px;
  border-radius: 5px;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.choose-recomendation{
  margin: 20px 20px 8px 20px;
}

.choose-recomendation > svg {
  margin-right: 10px;
}

.choose-recomendation span {
  color: var(--text-default, #202223);
  font-feature-settings: 'clig' off, 'liga' off;
  font-family: Inter;
  font-size: 18px;
  font-style: normal;
  font-weight: 500;
  line-height: 28px; /* 155.556% */

}

.search {
  display: flex;
  width: 100%;
  align-items: center;
}

.search > svg {
  transform: translate(24px, 0px)
}

.search span {
  width: 100%;
  border-radius: 5px;
  margin-left: 20px;
  margin-top: 4px;
  margin-right: 23px;
}

.search input  {
  height: 44px;
}

.search .selected{
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 120px;
    height: 42px;
    border-radius: 0px 6px 6px 0px;
    border-top: 1.21px solid #E6E6E6;
    border-right: 1.21px solid #E6E6E6;
    border-bottom: 1.21px solid #E6E6E6;
}

.search .ant-select {
  width: 90%;
}

td{
  border-bottom: 1px groove #EFEFEF;
}

.table-product {
  width: 97%;
  height: 50%;
  margin-left: 1rem;
  margin-top: 1rem;
  overflow-y: auto;
}

.table-product .ant-table-thead {
  position: sticky ; top: 0px;
  background-color: #ffff;
  z-index: 5;
}
.table-product table td:first-child {
 text-align: center;
 width: 40px;
 height: 40px;
}

.table-product .col_image{
  text-align: center;
  width: 80px;
  height: 40px;
}

.table-product .col_name{
  width: 444px;
  height: 40px;
}

.table-product .col_price{
  width: 157px;
  height: 40px;
}

.table-product .col_compare_price{
  width: 204px;
  height: 40px;
}

.table-product .col_qty{
  width: 104px;
  height: 40px;
}

.table-row {
  height: 3rem;
  font-size: 14px;
}

input[type=checkbox]{
  width: 16px;
  height: 15px;
}

.selected_products {
  margin-left: 21px;
  margin-left: 21px;
    width: 100%;
    height: max-content;
    margin-top: 13px;
}

.selected_product {
  height: 24px;
  font-style: normal;
  font-weight: 400;
  border: 1px solid #E2E2E2;
  border-radius: 5px;
  font-size: 14px;
  background: white;
  margin-right: 15px;
  float: left;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  line-height: 17px;
  color: black;
}

.search-box{
  position: absolute;
  left: 37px;
  top: 98px;
  width: calc(100% - 200px);
  display: flex;
  padding: 8px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
  border-radius: 0px 0px 6px 6px;
  border: 1px solid #D1D1D1;
  background-color: #fff;
  z-index: 7;
  height: auto;
  overflow: auto;
}

.search-box .search-box-item{
  display: flex;
  padding: 12px 16px;
  background-color: #F4F4F4;
  border-radius: 8px;
  align-self: stretch;
}

.search-box-item > div {
  display: flex;
  align-items: center;
  gap: 0px;
  flex: 1 0 0;
}

.search-box-item:hover {
  cursor: pointer;
  background: #E9F6FF;
}

.search-box-item img {
  width: 44px;
  height: 44px;
  border-radius: 4px;
}

.search-box-item > div > div {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
  flex: 1 0 0;
}

.search-box-item .title {
  color: var(--Neutral-100, #1C1C1E);
  line-height: 20px;
}

.search-box .des{
  color: #636366;
  font-size: 12px;
  font-weight: 400;
  line-height: 18px;
}

.remove-btn {
  margin-left: 16px;
  margin-top: 16px;
  color: #F00;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  gap: 6px;
  cursor: pointer;
}
.table-filter__hide {
  position: sticky;
  left: 50%;
  top: 0;
  text-align: center;
  align-items: center;
  transform: translate(-50%, -15%);
  font-weight: 600;
  width: fit-content;
}
.disabled-row {
  pointer-events: none;
  color: #dcdcdc;
}
</style>
