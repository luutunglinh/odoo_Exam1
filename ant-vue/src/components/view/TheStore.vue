<template>
  <div class="table_content">
    <MToast
      v-if="showToast"
      :content="content">
    </MToast>
    <div class="table__header">
      <div class="table__header__name__store">
        <span>Manual Recommendation</span>
      </div>
      <div class="table__header__btn">
        <button class="btn btn-cancel">Discard</button>
        <button class="btn btn-next">Save</button>
      </div>
    </div>
    <div class="setting_widget">
      <div class="setting_widget--name">
        <span>Enable Widget</span>
      </div>
      <Switch v-model:checked="enable_widget" checked-children="ON" un-checked-children="OFF" />
    </div>
    <div :class="enable_widget ? '' : 'disabled-row '">
      <TheStoreProduct></TheStoreProduct>
      <TheStoreProduct></TheStoreProduct>
    </div>
  </div>
</template>
<script>
import TheStoreProduct from '../view/TheStoreProduct.vue'
import { AutoComplete, Switch, Empty, Table } from 'ant-design-vue'
import { SearchOutlined } from '@ant-design/icons-vue'
import MToast from '../base/MToast.vue'
export default {
  name: 'TheStore',
  components: {
    Switch,
    MToast,
    TheStoreProduct
  },
  watch: {
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
    // selectAllRecommendation () {
    //   this.list_recommendation = []
    //   if (this.tickAllRecommendation === true) {
    //     this.isDeleteShow = true
    //     for (const product of this.selected_products) {
    //       const data = {
    //         id: product.id,
    //         name: product.name,
    //         price: product.price,
    //         compare_at_price: product.compare_at_price,
    //         quantity: product.qty,
    //         url_img: product.url_img
    //       }
    //       this.list_recommendation.push(data)
    //     }
    //   } else {
    //     this.list_recommendation = []
    //     this.isDeleteShow = false
    //   }
    // },
    // select_recommedation (data) {
    //   if (!this.list_recommendation.includes(data.id)) {
    //     this.isDeleteShow = true
    //     this.list_recommendation.push(data.id)
    //   } else {
    //     this.isDeleteShow = true
    //     this.list_recommendation = [
    //       ...this.list_recommendation.filter((item) => {
    //         return item !== data.id
    //       })
    //     ]
    //   }

    //   if (this.list_recommendation.length > 0) {
    //     this.tickAllRecommendation = false
    //     this.isDeleteShow = true
    //   } else {
    //     this.isDeleteShow = false
    //   }

    //   // thay @change = "select_recommedation" nếu dùng code dưới
    //   // if (!data.target.checked) {
    //   //   this.list_recommendation = this.list_recommendation.filter(e => e.id !== data.target._value.id)
    //   // } else {
    //   //   this.list_recommendation.push(data.target._value)
    //   //   this.isDeleteShow = true
    //   //   console.log(this.list_recommendation)
    //   //   if (this.list_recommendation.length === this.filteredRecommendation.length) {
    //   //     this.tickAllRecommendation = true
    //   //   } else this.tickAllRecommendation = false
    //   // }
    // },
    // addProduct (data) {
    //   if ((this.selected_products.length < 5)) {
    //     if ((!this.selected_products.some(product => product.id === data.id))) {
    //       const dataSelectedProducts = {
    //         id: data.id,
    //         name: data.name,
    //         price: data.price,
    //         qty: data.qty,
    //         compare_at_price: data.compare_at_price,
    //         url_img: data.url_img
    //       }
    //       this.selected_products.push(dataSelectedProducts)
    //     }
    //   } else {
    //     this.showToast = true
    //     this.content = 'You have reach the product limitation. Please remove any products from the list to continue selecting'
    //     setTimeout((e) => {
    //       this.showToast = false
    //     }, 3000)
    //   }
    // },
    // deleteProducts () {
    //   console.log(this.selected_products.length, this.list_recommendation)
    //   if (this.selected_products.length === this.list_recommendation.length) {
    //     this.selected_products = []
    //     this.list_recommendation = []
    //   } else {
    //     this.selected_products = [...this.selected_products.filter(product => !this.list_recommendation.includes(product.id))]
    //     this.list_recommendation = []
    //     this.isDeleteShow = false
    //   }
    // }
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

.input {
  display: flex;
  align-items: center;
  padding-left: 20px;
  border: 1.21px solid #E6E6E6;
  border-radius: 6px 0px 0px 6px;
  width: 100%;
}

.table__header__name__store {
  margin-top: 40px;
  padding-left: 20px;
}

.table__header__name__store span {
  color: #000;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px;
}

.table__header__btn {
  margin-top: 40px;
  padding-right: 24px;
}

.setting_widget {
    display: flex;
    margin-left: 20px;
    align-items: center;
    margin-top: 30px;
    margin-bottom: 20px ;
}

.setting_widget--name {
  margin-right: 20px;
}

.setting_widget .setting_widget--name > span {
  color: #000;
  font-family: Inter;
  font-size: 18px;
  font-style: normal;
  font-weight: 600;
  line-height: 22px;
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

input[type=checkbox]{
  width: 16px;
  height: 15px;
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
.disabled-row {
  pointer-events: none;
  color: #dcdcdc;
}
</style>
