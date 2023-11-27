<template>
  <div class="table__content">
    <div class="table__header table__header__addproduct">
      <div class="table__header__name">
        <span>WELCOME, CHLOE NGUYEN!</span>
      </div>
    </div>
    <div class="table__container">
      <div class="table__container__wapper">
        <div class="table__container_data__table">
          <div class="table__operations" v-if="hasSelected">
            <Button @click="enableSelected()">
              <span> Enable selected store(s)</span>
            </Button>
            <Button @click="disableSelected()">
              <span>Disable selected store(s)</span>
            </Button>
          </div>
          <Table
            :row-selection="{ selectedRowKeys: selectedRowKeys, onChange: onSelectChange, onSelect: disableSelected }"
            :columns="columns"
            :data-source="test"
          >
          <template #bodyCell="{ column, record }">
            <template v-if="column.dataIndex === 'name'">
              <router-link to="/dashboard/thestore/:id">{{ record.name }}</router-link>
            </template>
            <template v-if="column.key === 'status'">
              <Switch v-model:checked="record.status" checked-children="ON" un-checked-children="OFF" />
            </template>
          </template>
        </Table>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Table, Button, Switch } from 'ant-design-vue'
export default {
  name: 'TheDashboard',
  components: {
    Table,
    Button,
    Switch
  },
  data () {
    return {
      columns: [
        {
          title: 'Name',
          dataIndex: 'name',
          key: 'name',
          width: '65%'
        },
        {
          title: 'Products included',
          dataIndex: 'product_number'
        },
        {
          title: 'Status',
          dataIndex: 'status',
          key: 'status'
        }
      ],
      test: [
        {
          key: 1,
          name: 'John Doe',
          product_number: 25,
          status: true
        },
        {
          key: 2,
          name: 'Jane Doe',
          product_number: 30,
          status: false
        }
      ],
      selectedRowKeys: []
    }
  },
  methods: {
    onSelectChange (selectedRowKeys) {
      this.selectedRowKeys = selectedRowKeys
    },
    enableSelected () {
      this.test = this.test.map(record => {
        if (this.selectedRowKeys.includes(record.key)) {
          return { ...record, status: true }
        }
        return record
      })
    },
    disableSelected () {
      this.test = this.test.map(record => {
        if (this.selectedRowKeys.includes(record.key)) {
          return { ...record, status: false }
        }
        return record
      })
    }
  },
  computed: {
    hasSelected () {
      return this.selectedRowKeys.length > 0
    }
  }
}
</script>
<style lang="css" scoped>
.table__header__addproduct{
  margin-top: 25px;
}
</style>
