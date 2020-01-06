import Vue from 'vue'
import Router from 'vue-router'
// import OpenForm from './../pages/openform/openForm'
import FormSummary from './../components/FormSummary'
import OpenFormView from './../pages/openformView/openformView'


import FormList from './../components/FormList'
import ControlPanel from './../components/ControlPanel'
import Register from '../components/Register'

import OpenFormSetting from './../components/openform/openForm'

import Login from './../components/Login'

import OpenForm from './../pages/openform/openForm'

import FormData from '../components/formData/FormData'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'OpenForm',
    //   component: OpenForm
    // },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },{
      path: '/',
      name: 'OpenFormView',
      component: OpenFormView,
      children: [
        { path: '/form/:id/', name: "cp_form_summary", component: FormSummary},
        { path: '/', component: FormList},
        { path: '/formData', name: "FormData", component: FormData},
      ]
    },{
      path: '/openform',
      name: 'OpenForm',
      component: OpenForm,
      children: [
        { path: '/', component: OpenFormSetting},
      ]
    },
    {
      path: '/cp', component: ControlPanel,
      children: [
        { path: 'form/', name: 'cp_form_list', component: FormList},
        { path: 'form/:id/', name: "cp_form_summary", component: FormSummary},

      ]
    },
  ]
})
