import { request } from '@/api/service'
// 指定接口的基础路径
export const urlPrefix = '/api/crud_demo/'

// 获取列表函数
export function GetList(query) {
  return request({
    url: urlPrefix,
    method: 'get',
    params: query
  })
}
// 添加数据
export function AddObj(obj) {
  return request({
    url: urlPrefix,
    method: 'post',
    data: obj
  })
}
// 更新数据
export function UpdateObj(obj) {
  return request({
    url: urlPrefix + obj.id + '/',
    method: 'put',
    data: obj
  })
}
// 删除数据
export function DelObj(id) {
  return request({
    url: urlPrefix + id + '/',
    method: 'delete',
    data: { id }
  })
}