// Pagaya Technologies Q2 2026 Earnings Report - Charts
(function() {
'use strict';

// Common color palette
const colors = {
  blue: '#0071e3', green: '#34c759', orange: '#ea8600', red: '#d93025',
  purple: '#af52de', teal: '#5ac8fa', gray: '#8e8e93',
  blueLight: '#409cff', greenLight: '#30d158', orangeLight: '#ff9f0a'
};

// ============ Chart 1: Revenue & Net Income Trend (8 quarters) ============
(function() {
  var dom = document.getElementById('chart-revenue-trend');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'axis' },
    legend: { data: ['Network Volume ($B)', 'Total Revenue ($M)', 'GAAP Net Income ($M)'], bottom: 0 },
    grid: { left: '3%', right: '4%', bottom: '15%', top: '10%', containLabel: true },
    xAxis: { type: 'category', data: ['Q3 2024','Q4 2024','Q1 2025','Q2 2025','Q3 2025','Q4 2025','Q1 2026','Q2 2026'] },
    yAxis: [
      { type: 'value', name: 'Network Volume ($B)', axisLabel: { formatter: '{value}B' } },
      { type: 'value', name: 'Revenue/Income ($M)', axisLabel: { formatter: '{value}M' } }
    ],
    series: [
      { name: 'Network Volume ($B)', type: 'bar', yAxisIndex: 0, data: [2.3, 2.4, 2.5, 2.6, 2.8, 2.9, 3.0, 3.5], color: colors.blueLight, barWidth: '40%' },
      { name: 'Total Revenue ($M)', type: 'line', yAxisIndex: 1, data: [230, 276, 283, 318, 340, 321, 318, 387], color: colors.green, smooth: true },
      { name: 'GAAP Net Income ($M)', type: 'line', yAxisIndex: 1, data: [-11, -238, 8, 17, 23, 34, 25, 45], color: colors.orange, smooth: true, lineStyle: { type: 'dashed' } }
    ]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 2: Revenue Mix (Pie) ============
(function() {
  var dom = document.getElementById('chart-revenue-mix');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
    legend: { orient: 'vertical', left: 'left', top: 'center' },
    series: [{
      type: 'pie', radius: ['40%', '70%'], center: ['55%', '50%'],
      data: [
        { value: 250, name: 'Fee Revenue', itemStyle: { color: colors.blue } },
        { value: 137, name: 'Interest Income', itemStyle: { color: colors.green } }
      ],
      label: { formatter: '{b}\n{d}%' },
      emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0,0,0,0.5)' } }
    }]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 3: Margin Trend ============
(function() {
  var dom = document.getElementById('chart-margin-trend');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'axis' },
    legend: { data: ['Adjusted EBITDA Margin', 'Operating Margin', 'Net Margin'], bottom: 0 },
    grid: { left: '3%', right: '4%', bottom: '15%', top: '10%', containLabel: true },
    xAxis: { type: 'category', data: ['Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026', 'Q2 2026'] },
    yAxis: { type: 'value', axisLabel: { formatter: '{value}%' }, max: 40 },
    series: [
      { name: 'Adjusted EBITDA Margin', type: 'line', data: [27, 28, 29, 30, 32], color: colors.blue, smooth: true, areaStyle: { opacity: 0.1 } },
      { name: 'Operating Margin', type: 'line', data: [17.5, 23.5, 20.5, 25.2, 27.4], color: colors.green, smooth: true },
      { name: 'Net Margin', type: 'line', data: [5.2, 6.6, 10.7, 7.8, 11.6], color: colors.orange, smooth: true, lineStyle: { type: 'dashed' } }
    ]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 4: Cash Flow Structure ============
(function() {
  var dom = document.getElementById('chart-cashflow');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'axis' },
    legend: { data: ['Operating CF', 'Investing CF', 'Financing CF', 'Free CF'], bottom: 0 },
    grid: { left: '3%', right: '4%', bottom: '15%', top: '10%', containLabel: true },
    xAxis: { type: 'category', data: ['Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'] },
    yAxis: { type: 'value', axisLabel: { formatter: '{value}M' } },
    series: [
      { name: 'Operating CF', type: 'bar', data: [57, 67, 80, 43], color: colors.green },
      { name: 'Investing CF', type: 'bar', data: [-125, -57, -100, -16], color: colors.red },
      { name: 'Financing CF', type: 'bar', data: [78, 12, 43, 64], color: colors.blue },
      { name: 'Free CF', type: 'line', data: [54, 64, 77, 40], color: colors.orange, smooth: true, symbol: 'diamond', symbolSize: 10 }
    ]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 5: KPI Trend - Network Volume & FRLPC ============
(function() {
  var dom = document.getElementById('chart-kpi-trend');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'axis' },
    legend: { data: ['Network Volume ($B)', 'FRLPC ($M)', 'FRLPC %'], bottom: 0 },
    grid: { left: '3%', right: '4%', bottom: '15%', top: '10%', containLabel: true },
    xAxis: { type: 'category', data: ['Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026', 'Q2 2026'] },
    yAxis: [
      { type: 'value', name: 'Amount' },
      { type: 'value', name: 'FRLPC %', axisLabel: { formatter: '{value}%' } }
    ],
    series: [
      { name: 'Network Volume ($B)', type: 'bar', yAxisIndex: 0, data: [2.6, 2.8, 2.9, 3.0, 3.5], color: colors.blueLight, barWidth: '30%' },
      { name: 'FRLPC ($M)', type: 'bar', yAxisIndex: 0, data: [127, 133, 134, 135, 147], color: colors.green, barWidth: '30%' },
      { name: 'FRLPC %', type: 'line', yAxisIndex: 1, data: [4.81, 4.75, 4.62, 4.50, 4.20], color: colors.orange, smooth: true }
    ]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 6: Geographic / Segment Distribution ============
(function() {
  var dom = document.getElementById('chart-geo');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
    legend: { orient: 'vertical', left: 'left', top: 'center' },
    series: [{
      type: 'pie', radius: ['40%', '70%'], center: ['55%', '50%'],
      data: [
        { value: 60, name: 'Personal Loan', itemStyle: { color: colors.blue } },
        { value: 30, name: 'Auto Loan', itemStyle: { color: colors.green } },
        { value: 7, name: 'POS', itemStyle: { color: colors.orange } },
        { value: 3, name: 'SFR & Other', itemStyle: { color: colors.gray } }
      ],
      label: { formatter: '{b}\n{d}%' },
      emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0,0,0,0.5)' } }
    }]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

// ============ Chart 7: Radar - Comprehensive Assessment ============
(function() {
  var dom = document.getElementById('chart-radar');
  if (!dom) return;
  var chart = echarts.init(dom);
  var option = {
    tooltip: {},
    legend: { data: ['Q2 2025', 'Q2 2026'], bottom: 0 },
    radar: {
      center: ['50%', '45%'],
      radius: '65%',
      indicator: [
        { name: 'Growth', max: 100 },
        { name: 'Profitability', max: 100 },
        { name: 'Efficiency', max: 100 },
        { name: 'Liquidity', max: 100 },
        { name: 'Valuation', max: 100 }
      ]
    },
    series: [{
      type: 'radar',
      data: [
        { value: [55, 40, 55, 60, 70], name: 'Q2 2025', itemStyle: { color: colors.gray }, areaStyle: { opacity: 0.1 } },
        { value: [85, 75, 80, 70, 55], name: 'Q2 2026', itemStyle: { color: colors.blue }, areaStyle: { opacity: 0.2 } }
      ]
    }]
  };
  chart.setOption(option);
  window.addEventListener('resize', function() { chart.resize(); });
})();

})();