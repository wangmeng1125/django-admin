import { request } from '@/api/service';
// import { BUTTON_STATUS_NUMBER } from '@/config/button';
import { urlPrefix as bookPrefix } from './api';

export default {
  data() {
    return {
      url: `${bookPrefix}/book/`, // 对应的api接口路径
      crudOptions: null, // 保存crudOptions的变量
      dialogFormVisible: false, // 是否显示新增/编辑表单的变量
      formData: {}, // 表单数据
      formType: '', // 表单类型，是新增还是编辑
      formTitle: '', // 表单标题，新增或编辑
      formWidth: '35%', // 表单的宽度
      defaultSort: {}, // 表格的默认排序
      searchValue: '', // 搜索框的值
      selectedRows: [] // 选择的行数据
    };
  },

  created () {
    this.crudOptions = crudOptions(this);
  },

  methods: {
    // 表格的请求方法
    async getData(params) {
      const response = await request ({
        url: this.url,
        method: 'get',
        params
      });
      if (response.code === 200) {
        return response.data;
      } else {
        this.$message.error(response.message);
        return [];
      }
    },

    // 新增/编辑表单的提交方法
    async submitForm () {
      const isCreate = this.formType === 'create';
      const url = isCreate ? this.url : `${this.url}${this.formData.id}/`;
      const method = isCreate ? 'post' : 'put';
      const response = await request({
        url,
        method,
        data: this.formData
      });
      if (response.code === 200) {
        this.$message.success('保存成功');
        this.dialogFormVisible = false;
        this.getData();
      } else {
        this.$message.error(response.message);
      }
    },

    // 删除行数据的方法
    async removeRow (row) {
      const response = await request({
        url: `${this.url}${row.id}/`,
        method: 'delete'
      });
      if (response.code === 200) {
        this.$message.success('删除成功');
        this.getData();
      } else {
        this.$message.error(response.message);
      }
    },

    // 批量删除选中行数据的方法
    async removeSelectedRows () {
      const ids = this.selectedRows.map(item => item.id);
      const response = await request({
        url: `${this.url}delete_selected/`,
        method: 'post',
        data: {
          ids
        }
      });
      if (response.code === 200) {
        this.$message.success('批量删除成功');
        this.getData();
      } else {
        this.$message.error(response.message);
      }
    },

    // 重置表单数据的方法
    resetForm () {
      this.formData = {};
    },

    // 编辑行数据的方法
    editRow (row) {
      this.formData = { ...row };
      this.formType = 'update';
      this.formTitle = '编辑';
      this.dialogFormVisible = true;
    },

    // 新增行数据的方法
    createRow () {
      this.formData = {};
      this.formType = 'create';
      this.formTitle = '新增';
      this.dialogFormVisible = true;
    },
  }
}
// 表格的排序方法
// sortChange({ prop, order });
