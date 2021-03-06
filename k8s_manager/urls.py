# -*- coding: utf-8 -*-


"""k8s_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import home, assets, product, product_version, kube, kube_cluster, kube_install,kube_install_check,kube_install_step, storage_install


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home.index),

    #assets
    url(r'^assets$', assets.index),
    url(r'^assets/add$', assets.add),
    url(r'^assets/edit/(\d+)$', assets.edit),


    url(r'^product$', product.index),
    url(r'^product/add$', product.add),
    url(r'^product/edit/(\d+)$', product.edit),

    url(r'^product/version/(\d+)$', product_version.index),
    url(r'^product/version/add/(\d+)$', product_version.add),
   

    # storage相关
    url(r'^storage/install/add$', storage_install.add_storage),
    url(r'^storage/install/list$', storage_install.storage_list),
    url(r'^storage/install/edit/(\d+)$', storage_install.edit_storage),


    url(r'^k8s$', kube.index),
    # 编辑集群信息
    url(r'^k8s/add$', kube.add),
    url(r'^k8s/edit/(\d+)$', kube.edit),
    # 安装验证命令维护
    url(r'^k8s/command/add$', kube_install_check.add_check_command),
    url(r'^k8s/command/list$', kube_install_check.check_command_list),
    url(r'^k8s/command/edit/(\d+)$', kube_install_check.edit_check_command),

    # 安装部署维护
    url(r'^k8s/install/step/add$', kube_install_step.add_step),
    url(r'^k8s/install/step/list$', kube_install_step.step_list),
    url(r'^k8s/install/step/edit/(\d+)$', kube_install_step.edit_step),

    # 集群安装页面
    url(r'^k8s/install/(\d+)$', kube_install.install_index),

    # 执行集群安装命令
    url(r'^k8s/install/command/(\d+)/(-?\d+)$', kube_install.install_command),

    # 执行集群检测命令
    url(r'^k8s/check/command/(\d+)/(\d+)$', kube_install.install_check_command),

    # 删除k8s节点
    url(r'^k8s/remove/node/(\d+)/(\d+)$', kube_install.k8s_remove_node),


    # 编辑集群节点信息
    url(r'^k8s/cluster/(\d+)$', kube_cluster.index),
    url(r'^k8s/cluster/add/(\d+)$', kube_cluster.add),
    # url(r'^k8s/cluster/edit/(\d+)$', kube_cluster.edit),


]
