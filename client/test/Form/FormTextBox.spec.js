import FormTextBox from '@/components/Form/FormTextBox.vue';
import { mount } from '@vue/test-utils';

describe('FormTextBox', () => {
  it('is a Vue instance', () => {
    const wrapper = mount(FormTextBox);

    expect(wrapper.vm).toBeTruthy();
  });

  it('has a label', () => {
    const wrapper = mount(FormTextBox, { props: { header: 'Test TextBox' } });
    const label = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(label.text()).toBe('Test TextBox');
  });

  it('can show subtext', () => {
    const wrapper = mount(FormTextBox, {
      header: 'Test TextBox',
      subText: 'Test Subtext',
    });
    const subtext = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(subtext.text()).toBe('Test Subtext');
  });

  it('can make subtext a link', () => {
    const wrapper = mount(FormTextBox, {
      header: 'Test TextBox',
      subText: 'Test Subtext',
      subTextLink: '/login-page',
    });
    const subtext = wrapper.find('[data-test="formTextBoxLabel"]');

    expect(subtext.text()).toBe('Test Subtext');
    expect(subtext).toBeInstanceOf('a');
    expect(subtext).toHaveProperty('href', '/login-page');
  });
});
