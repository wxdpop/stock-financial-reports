/**
 * RKLB Q3 2026 财报报告图表脚本
 * ECharts SVG 渲染 / 无动画 / 响应式 / 7 个标准图表
 */
(function () {
  'use strict';
  var rootStyle = getComputedStyle(document.documentElement);
  function cssVar(name, fallback) {
    var v = rootStyle.getPropertyValue(name);
    v = v ? v.trim() : '';
    return v || fallback;
  }
  var palette = {
    primary:   cssVar('--color-primary',   '#2563eb'),
    accent:    cssVar('--color-accent',    '#0ea5e9'),
    positive:  cssVar('--color-positive',  '#16a34a'),
    negative:  cssVar('--color-negative',  '#dc2626'),
    neutral:   cssVar('--color-neutral',   '#64748b'),
    grid:      cssVar('--color-grid',      '#e2e8f0'),
    series1:   cssVar('--color-series-1',  '#2563eb'),
    series2:   cssVar('--color-series-2',  '#0ea5e9'),
    series3:   cssVar('--color-series-3',  '#f59e0b'),
    text:      cssVar('--color-text',      '#1e293b'),
    textMuted: cssVar('--color-text-muted','#64748b')
  };
  var isMobile = window.innerWidth <= 700;

  function baseOption() {
    return {
      animation: false,
      textStyle: { color: palette.text, fontFamily: "'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" },
      legend: { textStyle: { color: palette.textMuted } },
      tooltip: { trigger: 'axis', backgroundColor: 'rgba(255,255,255,0.96)', borderColor: palette.grid, textStyle: { color: palette.text } },
      grid: { left: isMobile ? 8 : 16, right: isMobile ? 8 : 20, top: isMobile ? 30 : 40, bottom: isMobile ? 40 : 20, containLabel: true },
      xAxis: { axisLine: { lineStyle: { color: palette.grid } }, axisLabel: { color: palette.textMuted, fontSize: isMobile ? 10 : 12, rotate: isMobile ? 30 : 0 }, axisTick: { show: false } },
      yAxis: { axisLine: { show: false }, axisTick: { show: false }, splitLine: { lineStyle: { color: palette.grid } }, axisLabel: { color: palette.textMuted, fontSize: isMobile ? 10 : 12 } }
    };
  }

  function render(elId, option) {
    var el = document.getElementById(elId);
    if (!el || typeof echarts === 'undefined') return;
    var chart = echarts.init(el, null, { renderer: 'svg' });
    chart.setOption(option);
    window.addEventListener('resize', function () { chart.resize(); });
  }

  /* 1. chart-revenue-trend：营收 + 净利润（百万美元） */
  render('chart-revenue-trend', Object.assign(baseOption(), {
    color: [palette.series1, palette.negative],
    legend: { data: ['营收', '净利润'], top: 0 },
    tooltip: { trigger: 'axis' },
    xAxis: Object.assign(baseOption().xAxis, { data: ['2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2', '2026Q3指引'] }),
    series: [
      { name: '营收', type: 'bar', data: [144.5, 155.1, 179.7, 200.4, 234.1, 257.5], itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] }, barWidth: isMobile ? 18 : 32 },
      { name: '净利润', type: 'line', yAxisIndex: 0, data: [-66.4, -18.3, -52.9, -45.0, -49.3, null], smooth: true, lineStyle: { width: 2 }, itemStyle: { color: palette.negative } }
    ]
  }));

  /* 2. chart-revenue-mix：营收构成（饼图） */
  render('chart-revenue-mix', Object.assign(baseOption(), {
    color: [palette.series1, palette.accent],
    tooltip: { trigger: 'item' },
    legend: { bottom: 0, textStyle: { color: palette.textMuted } },
    series: [{
      name: '营收构成', type: 'pie', radius: ['42%', '68%'],
      label: { formatter: '{b}\n{d}%', color: palette.textMuted, fontSize: isMobile ? 10 : 12 },
      data: [
        { name: '空间系统', value: 189.5 },
        { name: '发射服务', value: 44.6 }
      ]
    }]
  }));

  /* 3. chart-margin-trend：GAAP 毛利率趋势（%） */
  render('chart-margin-trend', Object.assign(baseOption(), {
    color: [palette.series3],
    tooltip: { trigger: 'axis' },
    xAxis: Object.assign(baseOption().xAxis, { data: ['2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2', '2026Q3指引'] }),
    yAxis: Object.assign(baseOption().yAxis, { max: 50, axisLabel: { color: palette.textMuted, fontSize: isMobile ? 10 : 12, formatter: '{value}%' } }),
    series: [{ name: '毛利率', type: 'bar', data: [32.1, 37.0, 38.0, 38.2, 36.1, 30.0], itemStyle: { color: function (p) { return p.dataIndex === 5 ? palette.neutral : palette.series3; }, borderRadius: [3, 3, 0, 0] }, barWidth: isMobile ? 18 : 32 }]
  }));

  /* 4. chart-cashflow：现金储备（百万美元） */
  render('chart-cashflow', Object.assign(baseOption(), {
    color: [palette.positive],
    tooltip: { trigger: 'axis' },
    xAxis: Object.assign(baseOption().xAxis, { data: ['2025Q3', '2025Q4', '2026Q1', '2026Q2'] }),
    series: [{ name: '现金及等价物', type: 'bar', data: [807.9, 828.7, 1205.0, 2129.0], itemStyle: { color: palette.positive, borderRadius: [3, 3, 0, 0] }, barWidth: isMobile ? 22 : 40 }]
  }));

  /* 5. chart-kpi-trend：营收（柱）+ 同比增速（线，%） */
  render('chart-kpi-trend', Object.assign(baseOption(), {
    color: [palette.series1, palette.series2],
    legend: { data: ['营收', '同比增速'], top: 0 },
    tooltip: { trigger: 'axis' },
    xAxis: Object.assign(baseOption().xAxis, { data: ['2025Q2', '2025Q3', '2025Q4', '2026Q1', '2026Q2'] }),
    yAxis: [
      Object.assign(baseOption().yAxis, {}),
      Object.assign(baseOption().yAxis, { splitLine: { show: false }, axisLabel: { color: palette.textMuted, fontSize: isMobile ? 10 : 12, formatter: '{value}%' } })
    ],
    series: [
      { name: '营收', type: 'bar', data: [144.5, 155.1, 179.7, 200.4, 234.1], itemStyle: { color: palette.series1, borderRadius: [3, 3, 0, 0] }, barWidth: isMobile ? 18 : 32 },
      { name: '同比增速', type: 'line', yAxisIndex: 1, data: [36.0, 48.0, 35.7, 63.5, 62.0], smooth: true, lineStyle: { width: 2 }, itemStyle: { color: palette.series2 } }
    ]
  }));

  /* 6. chart-geo：地区占比（饼图） */
  render('chart-geo', Object.assign(baseOption(), {
    color: [palette.series1, palette.accent],
    tooltip: { trigger: 'item' },
    legend: { bottom: 0, textStyle: { color: palette.textMuted } },
    series: [{
      name: '地区营收', type: 'pie', radius: ['42%', '68%'],
      label: { formatter: '{b}\n{d}%', color: palette.textMuted, fontSize: isMobile ? 10 : 12 },
      data: [
        { name: '美国', value: 80 },
        { name: '欧洲及国际', value: 20 }
      ]
    }]
  }));

  /* 7. chart-radar：综合财务指标（归一化 0-100） */
  render('chart-radar', Object.assign(baseOption(), {
    color: [palette.series1],
    tooltip: { trigger: 'item' },
    radar: {
      indicator: [
        { name: '营收增速', max: 100 },
        { name: '毛利率', max: 100 },
        { name: '盈利改善', max: 100 },
        { name: '现金储备', max: 100 },
        { name: '订单能见度', max: 100 },
        { name: '财务稳健', max: 100 }
      ],
      splitArea: { areaStyle: { color: ['rgba(37,99,235,0.02)', 'rgba(37,99,235,0.05)'] } },
      splitLine: { lineStyle: { color: palette.grid } },
      axisLine: { lineStyle: { color: palette.grid } },
      axisName: { color: palette.textMuted, fontSize: isMobile ? 10 : 12 }
    },
    series: [{ name: 'RKLB 综合', type: 'radar', data: [{ value: [85, 70, 72, 92, 95, 83], name: '综合指标' }], areaStyle: { opacity: 0.15 }, lineStyle: { width: 2 } }]
  }));
})();
